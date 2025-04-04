/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Canvg } from 'canvg'
import {
  IconButton, Tooltip, Drawer, List, ListItem, ListItemIcon, ListItemText, Divider, useMediaQuery, Snackbar
} from '@material-ui/core'
import AddBoxOutlinedIcon from '@material-ui/icons/AddBoxOutlined'
import PlayCircleOutlineIcon from '@material-ui/icons/PlayCircleOutline'
import DescriptionIcon from '@material-ui/icons/Description'
import HelpOutlineIcon from '@material-ui/icons/HelpOutline'
import UndoIcon from '@material-ui/icons/Undo'
import RedoIcon from '@material-ui/icons/Redo'
import ZoomInIcon from '@material-ui/icons/ZoomIn'
import ZoomOutIcon from '@material-ui/icons/ZoomOut'
import DeleteIcon from '@material-ui/icons/Delete'
import SettingsOverscanIcon from '@material-ui/icons/SettingsOverscan'
import PrintOutlinedIcon from '@material-ui/icons/PrintOutlined'
import RotateRightIcon from '@material-ui/icons/RotateRight'
// import BorderClearIcon from '@material-ui/icons/BorderClear'
import { makeStyles } from '@material-ui/core/styles'
import CloseIcon from '@material-ui/icons/Close'
import SaveOutlinedIcon from '@material-ui/icons/SaveOutlined'
import OpenInBrowserIcon from '@material-ui/icons/OpenInBrowser'
import ClearAllIcon from '@material-ui/icons/ClearAll'
import CreateNewFolderOutlinedIcon from '@material-ui/icons/CreateNewFolderOutlined'
import ImageOutlinedIcon from '@material-ui/icons/ImageOutlined'
import SystemUpdateAltOutlinedIcon from '@material-ui/icons/SystemUpdateAltOutlined'
import { Link as RouterLink } from 'react-router-dom'
import beautify from 'xml-beautifier'
import mxGraphFactory from 'mxgraph'

import { NetlistModal, HelpScreen, ImageExportDialog, OpenSchDialog, ScriptScreen } from './ToolbarExtension'
import { editorZoomIn, editorZoomOut, editorZoomAct, deleteComp, PrintPreview, Rotate, editorUndo, editorRedo, saveXml, ClearGrid } from './Helper/ToolbarTools'
import { useSelector, useDispatch } from 'react-redux'
import { toggleSimulate, closeCompProperties, setSchXmlData, saveSchematic, openLocalSch, setLoadingDiagram } from '../../redux/actions/index'
import api from '../../utils/Api'
import { transformXcos, saveToFile } from '../../utils/GalleryUtils'

const {
  mxUtils
} = new mxGraphFactory()

const useStyles = makeStyles((theme) => ({
  menuButton: {
    marginLeft: 'auto',
    marginRight: theme.spacing(0),
    padding: theme.spacing(1),
    [theme.breakpoints.up('lg')]: {
      display: 'none'
    }
  },
  tools: {
    padding: theme.spacing(1),
    margin: theme.spacing(0, 0.5),
    color: '#262626'
  },
  pipe: {
    fontSize: '1.45rem',
    color: '#d6c4c2',
    margin: theme.spacing(0, 1.5)
  }
}))

// Notification snackbar to give alert messages
function SimpleSnackbar ({ open, close, message }) {
  return (
    <div>
      <Snackbar
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'left'
        }}
        open={open}
        autoHideDuration={5000}
        onClose={close}
        message={message}
        action={
          <>
            <IconButton size='small' aria-label='close' color='inherit' onClick={close}>
              <CloseIcon fontSize='small' />
            </IconButton>
          </>
        }
      />
    </div>
  )
}

SimpleSnackbar.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  message: PropTypes.string
}

export default function SchematicToolbar ({ mobileClose, gridRef }) {
  const classes = useStyles()
  const isAuthenticated = useSelector(state => state.authReducer.isAuthenticated)
  const description = useSelector(state => state.saveSchematicReducer.description)
  const title2 = useSelector(state => state.saveSchematicReducer.title)

  const scriptDump = useSelector(state => state.saveSchematicReducer.scriptDump)

  const dispatch = useDispatch()
  const isMobile = useMediaQuery('(max-width:600px)')
  const [drawerOpen, setDrawerOpen] = useState(false)
  const toggleDrawer = (open) => () => setDrawerOpen(open)

  // Netlist Modal Control
  const [open, setOpen] = useState(false)
  const [netlist] = useState('')
  const handleNetlistOpen = () => {
    dispatch(toggleSimulate())
  }

  const handleClose = () => {
    setOpen(false)
  }

  // Control Help dialog window
  const [helpOpen, setHelpOpen] = useState(false)
  const [scriptOpen, setScriptOpen] = useState(false)

  const handleHelpOpen = () => {
    setHelpOpen(true)
  }

  const handleHelpClose = () => {
    setHelpOpen(false)
  }

  const handleSchWinOpen = () => {
    setScriptOpen(true)
  }

  const handleScriptClose = () => {
    setScriptOpen(false)
  }

  // Handle Delete component
  const handleDeleteComp = () => {
    deleteComp()
    dispatch(closeCompProperties())
  }

  // Handle Notification Snackbar
  const [snacOpen, setSnacOpen] = useState(false)
  const [message, setMessage] = useState('')

  const handleSnacClick = () => {
    setSnacOpen(true)
  }

  const handleSnacClose = (event, reason) => {
    if (reason === 'clickaway') {
      return
    }
    setSnacOpen(false)
  }

  // Image Export of Schematic Diagram
  async function exportImage (type) {
    try {
      const svg = document.querySelector('#divGrid > svg').cloneNode(true)

      // Ensure xlink namespace is declared in the root SVG element
      svg.setAttributeNS('http://www.w3.org/2000/xmlns/',
        'xmlns:xlink',
        'http://www.w3.org/1999/xlink')

      svg.removeAttribute('style')
      svg.setAttribute('width', gridRef.current.scrollWidth)
      svg.setAttribute('height', gridRef.current.scrollHeight)

      // Create a copy of the SVG for further processing if needed
      const svgCopyForCanvg = svg.cloneNode(true)

      const canvas = document.createElement('canvas')
      canvas.width = gridRef.current.scrollWidth
      canvas.height = gridRef.current.scrollHeight
      canvas.style.width = canvas.width + 'px'
      canvas.style.height = canvas.height + 'px'
      const images = svgCopyForCanvg.getElementsByTagName('image')
      for (const image of images) {
        try {
          const imageUrl = image.getAttribute('xlink:href')
          if (imageUrl) {
            let data = await fetch(imageUrl).then(v => v.text())
            data = encodeURIComponent(data)
            image.removeAttribute('xlink:href')
            image.setAttributeNS('http://www.w3.org/1999/xlink',
              'href',
              'data:image/svg+xml;base64,' + window.btoa(data)
            )
          }
        } catch (err) {
          console.error('Error fetching image data:', err)
          throw err
        }
      }
      const ctx = canvas.getContext('2d')
      ctx.webkitImageSmoothingEnabled = true
      ctx.msImageSmoothingEnabled = true
      ctx.imageSmoothingEnabled = true
      const pixelRatio = window.devicePixelRatio || 1
      ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0)
      return new Promise(resolve => {
        if (type === 'SVG') {
          const svgdata = new XMLSerializer().serializeToString(svg)
          resolve('<?xml version="1.0" encoding="UTF-8"?>' + svgdata)
          return
        }
        let svgString = svg.outerHTML
        svgString = svgString.replace(/<hr>/g, '<hr />').replace(/<br>/g, '<br />').replace(/&nbsp;/g, ' ')
        const v = Canvg.fromString(ctx, svgString)
        v.render().then(() => {
          let image = ''
          if (type === 'JPG') {
            const imgdata = ctx.getImageData(0, 0, canvas.width, canvas.height)
            for (let i = 0; i < imgdata.data.length; i += 4) {
              if (imgdata.data[i + 3] === 0) {
                imgdata.data[i] = 255
                imgdata.data[i + 1] = 255
                imgdata.data[i + 2] = 255
                imgdata.data[i + 3] = 255
              }
            }
            ctx.putImageData(imgdata, 0, 0)
            image = canvas.toDataURL('image/jpeg', 1.0)
          } else if (type === 'PNG') {
            image = canvas.toDataURL('image/png')
          }
          resolve(image)
        }).catch(err => {
          console.error('Error rendering SVG with Canvg:', err)
        })
      })
    } catch (err) {
      console.error('Error in exportImage function:', err)
    }
  }

  // Download JPEG, PNG exported Image
  function downloadImage (data, type) {
    const evt = new MouseEvent('click', {
      view: window,
      bubbles: false,
      cancelable: true
    })
    const a = document.createElement('a')
    const ext = (type === 'PNG') ? '.png' : '.jpg'
    a.setAttribute('download', title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud' + ext)
    a.setAttribute('href', data)
    a.setAttribute('target', '_blank')
    a.dispatchEvent(evt)
  }

  // Download SVG image
  function downloadText (data, options) {
    saveToFile(title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.svg', options, data)
  }

  const [imgopen, setImgOpen] = useState(false)

  const handleImgClickOpen = () => {
    setImgOpen(true)
  }

  const handleImgClose = (value) => {
    setImgOpen(false)
    if (value === 'SVG') {
      exportImage('SVG')
        .then(v => {
          downloadText(v, 'data:image/svg+xml')
        })
    } else if (value === 'PNG') {
      exportImage('PNG')
        .then(v => {
          downloadImage(v, 'PNG')
        })
    } else if (value === 'JPG') {
      exportImage('JPG')
        .then(v => {
          downloadImage(v, 'JPG')
        })
    }
  }

  // Handle Save Schematic onCloud
  const handleSchSave = () => {
    if (isAuthenticated !== true) {
      setMessage('You are not Logged In')
      handleSnacClick()
    } else {
      const xml = saveXml(description)
      dispatch(setSchXmlData(xml))
      exportImage('PNG')
        .then(res => {
          dispatch(saveSchematic(title2, description, xml, res, scriptDump))
          setMessage('Saved Successfully')
        })
        .catch(err => {
          // Debugging: Log if there is an error in exportImage
          console.error('Error exporting image:', err)
          setMessage('Error exporting image')
        })

      handleSnacClick()
    }
  }

  // Save Schematics Locally
  const handleLocalSchSave = () => {
    saveToFile(title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.xml', 'application/xml', beautify(saveXml(description)))
  }

  const handleLocalSchSaveXcos = async () => {
    try {
      const xmlContent = beautify(saveXml(description))
      const xmlBlob = new Blob([xmlContent], { type: 'application/xml' })

      const xmlFileName = title2 + '.xml'

      const formData = new FormData()
      formData.append('file', xmlBlob, xmlFileName)

      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      const response = await api.post('/simulation/save', formData, config)

      if (!response || response.status !== 200) {
        throw new Error('Network response was not ok')
      }
      saveToFile(title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.xcos', 'application/x-scilab-xcos', response.data)
    } catch (error) {
      console.error('There was an error!', error)
    }
  }

  const handleLocalSchSaveScript = () => {
    saveToFile(title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.sce', 'application/x-scilab', scriptDump)
  }

  const readXmlFile = (xmlDoc, dataDump, title) => {
    const firstCell = xmlDoc.documentElement.children[0].children[0]
    const firstCellAttrs = firstCell.attributes
    const appname = firstCellAttrs.appname.value
    const description = (firstCellAttrs.description !== undefined) ? firstCellAttrs.description.value : ''
    if (appname !== process.env.REACT_APP_NAME) {
      setMessage('Unsupported app name error !')
      handleSnacClick()
    } else {
      const obj = { data_dump: dataDump, title, description }
      if (obj.data_dump === undefined || obj.title === undefined || obj.description === undefined) {
        setMessage('Unsupported file error !')
        handleSnacClick()
      } else {
        dispatch(openLocalSch(obj))
      }
    }
  }

  // Open Locally Saved Schematic
  const handleLocalSchOpen = () => {
    const fileSelector = document.createElement('input')
    fileSelector.setAttribute('type', 'file')
    fileSelector.setAttribute('accept', '.xcos, .xml, application/xml')
    fileSelector.click()
    fileSelector.addEventListener('change', function (event) {
      const file = event.target.files[0]
      const filename = file.name
      const base = '(_' + process.env.REACT_APP_NAME + '_on_Cloud)?( *\\([0-9]*\\))?\\.(xcos|xml)$'
      const re = new RegExp(base, 'i')
      if (re.test(filename)) {
        const reader = new FileReader()
        reader.onload = function (event) {
          dispatch(setLoadingDiagram(true))
          const title = filename.replace(re, '')
          let dataDump = event.target.result
          const xmlDoc = mxUtils.parseXml(dataDump)
          const rexcos = /\.xcos$/i
          if (rexcos.test(filename)) {
            transformXcos(xmlDoc).then(xmlDoc => {
              dataDump = new XMLSerializer().serializeToString(xmlDoc)
              readXmlFile(xmlDoc, dataDump, title)
              dispatch(setLoadingDiagram(false))
            })
          } else {
            readXmlFile(xmlDoc, dataDump, title)
            dispatch(setLoadingDiagram(false))
          }
        }
        reader.readAsText(file)
      } else {
        setMessage('Unsupported file type error! Select valid file.')
        handleSnacClick()
      }
    })
  }

  // Control Help dialog window open and close
  const [schOpen, setSchOpen] = useState(false)

  const handleSchDialOpen = () => {
    setSchOpen(true)
  }

  const handleSchDialClose = () => {
    setSchOpen(false)
  }

  // All toolbar icons in order
  const toolbarItems = [
    { icon: <CreateNewFolderOutlinedIcon fontSize='small' />, label: 'New', link: '/editor' },
    { icon: <OpenInBrowserIcon fontSize='small' />, label: 'Open', action: handleSchDialOpen },
    { icon: <SaveOutlinedIcon fontSize='small' />, label: 'Save', action: handleSchSave },
    'pipe',
    { icon: <SystemUpdateAltOutlinedIcon fontSize='small' />, label: 'Export', action: handleLocalSchSave },
    { icon: <SystemUpdateAltOutlinedIcon fontSize='small' />, label: 'Export in Xcos', action: handleLocalSchSaveXcos },
    { icon: <SystemUpdateAltOutlinedIcon fontSize='small' />, label: 'Export Script', action: handleLocalSchSaveScript },
    { icon: <ImageOutlinedIcon fontSize='small' />, label: 'Image Export', action: handleImgClickOpen },
    { icon: <PrintOutlinedIcon fontSize='small' />, label: 'Print Preview', action: PrintPreview },
    'pipe',
    { icon: <DescriptionIcon fontSize='small' style={{ color: scriptDump ? 'red' : 'inherit' }} />, label: 'Show Script', action: handleSchWinOpen },
    { icon: <PlayCircleOutlineIcon fontSize='small' />, label: 'Simulate', action: handleNetlistOpen },
    'pipe',
    { icon: <UndoIcon fontSize='small' />, label: 'Undo', action: editorUndo },
    { icon: <RedoIcon fontSize='small' />, label: 'Redo', action: editorRedo },
    { icon: <RotateRightIcon fontSize='small' />, label: 'Rotate', action: Rotate },
    'pipe',
    { icon: <ZoomInIcon fontSize='small' />, label: 'Zoom In', action: editorZoomIn },
    { icon: <ZoomOutIcon fontSize='small' />, label: 'Zoom Out', action: editorZoomOut },
    { icon: <SettingsOverscanIcon fontSize='small' />, label: 'Default Size', action: editorZoomAct },
    'pipe',
    { icon: <DeleteIcon fontSize='small' />, label: 'Delete', action: handleDeleteComp },
    { icon: <ClearAllIcon fontSize='small' />, label: 'Clear All', action: ClearGrid },
    { icon: <HelpOutlineIcon fontSize='small' />, label: 'Help', action: handleHelpOpen }
  ]

  // Only first 7 icons will be shown in mobile view, rest will go into the drawer
  const visibleIcons = isMobile ? toolbarItems.slice(0, 7) : toolbarItems

  return (
    <>
      <div style={{ display: 'flex', gap: '2px', alignItems: 'center' }}>
        {/* ✅ Desktop: Show all icons */}
        {!isMobile && visibleIcons.map((item, index) =>
          item === 'pipe'
            ? (
              <span key={index} style={{ margin: '0 8px', fontWeight: 'bold', opacity: 0.7, fontSize: '18px' }}>|</span>
              )
            : (
              <Tooltip key={index} title={item.label}>
                {item.link
                  ? (
                    <IconButton color='inherit' className={classes.tools} size='small' component={RouterLink} to={item.link}>
                      {item.icon}
                    </IconButton>
                    )
                  : (
                    <IconButton color='inherit' className={classes.tools} size='small' onClick={item.action}>
                      {item.icon}
                    </IconButton>
                    )}
              </Tooltip>
              )
        )}

        {/* ✅ Mobile: Show only hamburger menu */}
        {isMobile && (
          <>
            <Tooltip title="More">
              <IconButton
                color='inherit'
                aria-label='open drawer'
                edge='end'
                size='small'
                onClick={toggleDrawer(true)}
                className={classes.menuButton}
              >
                <AddBoxOutlinedIcon fontSize='small' />
              </IconButton>
            </Tooltip>
          </>
        )}
      </div>

      {/* ✅ Mobile Hamburger Drawer */}
      <Drawer anchor="right" open={drawerOpen} onClose={toggleDrawer(false)}>
        <List>
          {toolbarItems.map((item, index) =>
            item === 'pipe'
              ? <Divider key={index} />
              : (
                <ListItem button key={index} onClick={item.action}>
                  <ListItemIcon>{item.icon}</ListItemIcon>
                  <ListItemText primary={item.label} />
                </ListItem>
                )
          )}
          <Divider />
          <ListItem button onClick={toggleDrawer(false)}>
            <ListItemText primary="Close Menu" />
          </ListItem>
        </List>
      </Drawer>

      {/* ✅ Dialogs & Modals */}
      <OpenSchDialog open={schOpen} close={handleSchDialClose} openLocal={handleLocalSchOpen} />
      <SimpleSnackbar open={snacOpen} close={handleSnacClose} message={message} />
      <ImageExportDialog open={imgopen} onClose={handleImgClose} />
      <NetlistModal open={open} close={handleClose} netlist={netlist} />
      <HelpScreen open={helpOpen} close={handleHelpClose} />
      <ScriptScreen isOpen={scriptOpen} onClose={handleScriptClose} />
    </>
  )
}

SchematicToolbar.propTypes = {
  mobileClose: PropTypes.func,
  gridRef: PropTypes.object.isRequired
}
