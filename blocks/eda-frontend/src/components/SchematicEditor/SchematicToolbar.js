/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Canvg } from 'canvg'
import { Link as RouterLink } from 'react-router-dom'
import beautify from 'xml-beautifier'
import mxGraphFactory from 'mxgraph'
import { useSelector, useDispatch } from 'react-redux'

import { IconButton, Tooltip, Snackbar } from '@mui/material'
import AddBoxOutlinedIcon from '@mui/icons-material/AddBoxOutlined'
import BorderClearIcon from '@mui/icons-material/BorderClear'
import ClearAllIcon from '@mui/icons-material/ClearAll'
import CloseIcon from '@mui/icons-material/Close'
import CreateNewFolderOutlinedIcon from '@mui/icons-material/CreateNewFolderOutlined'
import DeleteIcon from '@mui/icons-material/Delete'
import HelpOutlineIcon from '@mui/icons-material/HelpOutline'
import ImageOutlinedIcon from '@mui/icons-material/ImageOutlined'
import OpenInBrowserIcon from '@mui/icons-material/OpenInBrowser'
import PlayCircleOutlineIcon from '@mui/icons-material/PlayCircleOutline'
import PrintOutlinedIcon from '@mui/icons-material/PrintOutlined'
import RedoIcon from '@mui/icons-material/Redo'
import RotateRightIcon from '@mui/icons-material/RotateRight'
import SaveOutlinedIcon from '@mui/icons-material/SaveOutlined'
import SettingsOverscanIcon from '@mui/icons-material/SettingsOverscan'
import SystemUpdateAltOutlinedIcon from '@mui/icons-material/SystemUpdateAltOutlined'
import UndoIcon from '@mui/icons-material/Undo'
import ZoomInIcon from '@mui/icons-material/ZoomIn'
import ZoomOutIcon from '@mui/icons-material/ZoomOut'
import { makeStyles } from '@mui/styles'

import { NetlistModal, HelpScreen, ImageExportDialog, OpenSchDialog } from './ToolbarExtension'
import { editorZoomIn, editorZoomOut, editorZoomAct, deleteComp, PrintPreview, Rotate, generateNetList, editorUndo, editorRedo, saveXml, ClearGrid } from './Helper/ToolbarTools'
import api from '../../utils/Api'
import { transformXcos } from '../../utils/GalleryUtils'

import { toggleSimulate, closeCompProperties, setSchXmlData, saveSchematic, openLocalSch, setLoadingDiagram } from '../../redux/actions/index'

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
  const controlBlock = useSelector(state => state.netlistReducer.controlBlock)
  const controlLine = useSelector(state => state.netlistReducer.controlLine)
  const title1 = useSelector(state => state.netlistReducer.title)
  const isAuthenticated = useSelector(state => state.authReducer.isAuthenticated)
  const description = useSelector(state => state.saveSchematicReducer.description)
  const title2 = useSelector(state => state.saveSchematicReducer.title)

  const dispatch = useDispatch()

  // Netlist Modal Control
  const [open, setOpen] = useState(false)
  const [netlist, genNetlist] = useState('')

  const handleClickOpen = () => {
    const compNetlist = generateNetList()
    const netlist = title1 + '\n\n' +
      compNetlist.models + '\n' +
      compNetlist.main + '\n' +
      controlLine + '\n' +
      controlBlock + '\n'
    genNetlist(netlist)
    setOpen(true)
  }

  const handleClose = () => {
    setOpen(false)
  }

  // Control Help dialog window
  const [helpOpen, setHelpOpen] = useState(false)

  const handleHelpOpen = () => {
    setHelpOpen(true)
  }

  const handleHelpClose = () => {
    setHelpOpen(false)
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
        svgString = svgString.replace(/<hr>/g, '<hr />').replace(/<br>/g, '<br />')
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
    const blob = new Blob(data, options)
    const evt = new MouseEvent('click', {
      view: window,
      bubbles: false,
      cancelable: true
    })
    const a = document.createElement('a')
    a.setAttribute('download', title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.svg')
    a.href = URL.createObjectURL(blob)
    a.target = '_blank'
    a.setAttribute('target', '_blank')
    a.dispatchEvent(evt)
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
          downloadText([v], {
            type: 'data:image/svg+xml;charset=utf-8;'
          })
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
          dispatch(saveSchematic(title2, description, xml, res))
        })
        .catch(err => {
          // Debugging: Log if there is an error in exportImage
          console.error('Error exporting image:', err)
        })

      setMessage('Saved Successfully')
      handleSnacClick()
    }
  }

  // Save Schematics Locally
  const handleLocalSchSave = () => {
    const blob = new Blob([beautify(saveXml(description))], { type: 'application/xml' })
    const evt = new MouseEvent('click', {
      view: window,
      bubbles: false,
      cancelable: true
    })
    const a = document.createElement('a')
    a.setAttribute('download', title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.xml')
    a.href = URL.createObjectURL(blob)
    a.target = '_blank'
    a.setAttribute('target', '_blank')
    a.dispatchEvent(evt)
  }

  const handleLocalSchSaveXcos = async () => {
    try {
      const xmlContent = beautify(saveXml(description))
      const xmlBlob = new Blob([xmlContent], { type: 'application/xml' })

      const xmlFileName = title2 + '.xml'

      const formData = new FormData()
      formData.append('file', xmlBlob, xmlFileName)

      const response = await api.post('/simulation/save', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })

      if (!response || response.status !== 200) {
        throw new Error('Network response was not ok')
      }
      const xcosBlob = new Blob([response.data], { type: 'application/xcos' })

      const a = document.createElement('a')
      a.setAttribute('download', title2 + '_' + process.env.REACT_APP_NAME + '_on_Cloud.xcos')
      a.href = URL.createObjectURL(xcosBlob)
      a.target = '_blank'
      a.setAttribute('target', '_blank')

      const evt = new MouseEvent('click', {
        view: window,
        bubbles: false,
        cancelable: true
      })
      a.dispatchEvent(evt)
    } catch (error) {
      console.error('There was an error!', error)
    }
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

  return (
    <>
      <Tooltip title='New'>
        <IconButton color='inherit' className={classes.tools} size='small' target='_blank' component={RouterLink} to='/editor'>
          <CreateNewFolderOutlinedIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Open'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleSchDialOpen}>
          <OpenInBrowserIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <OpenSchDialog open={schOpen} close={handleSchDialClose} openLocal={handleLocalSchOpen} />
      <Tooltip title='Save'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleSchSave}>
          <SaveOutlinedIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <SimpleSnackbar open={snacOpen} close={handleSnacClose} message={message} />
      <span className={classes.pipe}>|</span>

      <Tooltip title='Export'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleLocalSchSave}>
          <SystemUpdateAltOutlinedIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Export in xcos'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleLocalSchSaveXcos}>
          <SystemUpdateAltOutlinedIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Image Export'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleImgClickOpen}>
          <ImageOutlinedIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <ImageExportDialog open={imgopen} onClose={handleImgClose} />
      <Tooltip title='Print Preview'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={PrintPreview}>
          <PrintOutlinedIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <span className={classes.pipe}>|</span>

      <Tooltip title='Simulate'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={() => { dispatch(toggleSimulate()) }}>
          <PlayCircleOutlineIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Generate Netlist'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleClickOpen}>
          <BorderClearIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <NetlistModal open={open} close={handleClose} netlist={netlist} />
      <span className={classes.pipe}>|</span>

      <Tooltip title='Undo'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={editorUndo}>
          <UndoIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Redo'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={editorRedo}>
          <RedoIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Rotate'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={Rotate}>
          <RotateRightIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <span className={classes.pipe}>|</span>

      <Tooltip title='Zoom In'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={editorZoomIn}>
          <ZoomInIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Zoom Out'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={editorZoomOut}>
          <ZoomOutIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Default Size'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={editorZoomAct}>
          <SettingsOverscanIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <span className={classes.pipe}>|</span>

      <Tooltip title='Delete'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleDeleteComp}>
          <DeleteIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Clear All'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={ClearGrid}>
          <ClearAllIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <Tooltip title='Help'>
        <IconButton color='inherit' className={classes.tools} size='small' onClick={handleHelpOpen}>
          <HelpOutlineIcon fontSize='small' />
        </IconButton>
      </Tooltip>
      <HelpScreen open={helpOpen} close={handleHelpClose} />

      <IconButton
        color='inherit'
        aria-label='open drawer'
        edge='end'
        size='small'
        onClick={mobileClose}
        className={classes.menuButton}
      >
        <AddBoxOutlinedIcon fontSize='small' />
      </IconButton>
    </>
  )
}

SchematicToolbar.propTypes = {
  mobileClose: PropTypes.func,
  gridRef: PropTypes.object.isRequired
}
