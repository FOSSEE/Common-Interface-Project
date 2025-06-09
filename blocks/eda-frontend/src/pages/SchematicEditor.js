// Main Layout for Schematic Editor page.
import { useEffect, useRef, useState } from 'react'
import PropTypes from 'prop-types'
import { TailSpin } from 'react-loader-spinner'
import { CssBaseline } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'

import Layout from '../components/Shared/Layout'
import Header from '../components/SchematicEditor/Header'
import ComponentSidebar, { ComponentImages } from '../components/SchematicEditor/ComponentSidebar'
import LayoutMain from '../components/Shared/LayoutMain'
import SchematicToolbar from '../components/SchematicEditor/SchematicToolbar'
import RightSidebar from '../components/SchematicEditor/RightSidebar'
import PropertiesSidebar from '../components/SchematicEditor/PropertiesSidebar'
import loadGrid from '../components/SchematicEditor/Helper/ComponentDrag'
import { getCurrentDiagramXML } from '../components/SchematicEditor/Helper/ComponentDrag'
import { renderGalleryXML } from '../components/SchematicEditor/Helper/ToolbarTools'
import '../components/SchematicEditor/Helper/SchematicEditor.css'
import { fetchDiagram, fetchSchematic } from '../redux/saveSchematicSlice'
import { useDispatch, useSelector } from 'react-redux'
import { styleToObject } from '../utils/GalleryUtils'
import { changePorts } from '../components/SchematicEditor/ComponentProperties'
import { graph } from '../components/SchematicEditor/Helper/ComponentDrag'
import mxGraphFactory from 'mxgraph'
const {
  mxPrintPreview,
  mxConstants,
  mxRectangle,
  mxUtils,
  mxUndoManager,
  mxEvent,
  mxCodec,
  mxPoint
} = new mxGraphFactory()

const useStyles = makeStyles((_theme) => ({
  root: {
    display: 'flex',
    minHeight: '100vh'
  },
  toolbar: {
    minHeight: '80px'
  }
}))

export default function SchematicEditor (props) {
  const classes = useStyles()
  const compRef = useRef()
  const gridRef = useRef()
  const outlineRef = useRef()
  const dispatch = useDispatch()
  const [mobileOpen, setMobileOpen] = useState(false)
  const isLoading = useSelector(state => state.saveSchematic.isLoading)
  const xmlData = useSelector(state => state.saveSchematic.xmlData)
  const [mainDiagramBackup, setMainDiagramBackup] = useState('')
  const [activeSuperBlockCell, setActiveSuperBlockCell] = useState(null)

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen)
  }


  function handleCloseClick () {
    if (!activeSuperBlockCell) return

    const updatedXML = getCurrentDiagramXML()
    // console.log('updatedXML::', updatedXML)
    const xml = '<SuperBlockDiagram as="child" background="-1" title="">' + updatedXML + '</SuperBlockDiagram>'
    const updatedDOM = mxUtils.parseXml(xml)
    const updatedDOM1 = updatedDOM.getElementsByTagName('SuperBlockDiagram')[0]
    activeSuperBlockCell.SuperBlockDiagram = updatedDOM1

    // Mapping block styles to port count fields
    const portMapping = {
      'IN_f': 'explicitInputPorts',
      'INIMPL_f': 'implicitInputPorts',
      'CLKINV_f': 'commandPorts',
      'OUT_f': 'explicitOutputPorts',
      'OUTIMPL_f': 'implicitOutputPorts',
      'CLKOUTV_f': 'controlPorts'
    }

    const xpath = "/SuperBlockDiagram/mxGraphModel/root/mxCell[@style]"
    const xpathResult = document.evaluate(
      xpath,
      activeSuperBlockCell.SuperBlockDiagram,
      null,
      XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
      null
    )

    const allCells = []
    for (let i = 0; i < xpathResult.snapshotLength; i++) {
      allCells.push(xpathResult.snapshotItem(i))
    }

    const styleCounts = {}

    allCells.forEach(cell => {
      console.log("CELL1", cell)
      const cellAttrs = cell.attributes
      console.log('cellAttrs:', cellAttrs)
      const style = cellAttrs.style.value
      const defaultStyle = styleToObject(style).default
      console.log("CELL2", defaultStyle)

      styleCounts[defaultStyle] = (styleCounts[defaultStyle] || 0) + 1

    })

    console.log('Style counts:', styleCounts)

    // Object.entries(styleCounts).forEach(([blockStyle, count]) => {
    //   const mapping = portMapping[blockStyle]
    //   console.log('mapping:', mapping)
    //   if (mapping) {
    //     activeSuperBlockCell[mapping] = count
    //   }

    // })
    console.log('activeSuperBlockCell1:', activeSuperBlockCell)

    if (activeSuperBlockCell) {
      const refreshDisplay = changePorts(
        activeSuperBlockCell,
        styleCounts['OUT_f'] || 0,
        styleCounts['OUTIMPL_f'] || 0,
        styleCounts['CLKOUTV_f'] || 0,
        styleCounts['IN_f'] || 0,
        styleCounts['INIMPL_f'] || 0,
        styleCounts['CLKINV_f'] || 0,
        false
      )

      console.log('blockElem:', activeSuperBlockCell, refreshDisplay)
      if (refreshDisplay) {
        graph.refresh()
      }

      // Remove existing <SuperBlockDiagram> child if present
      const existing = activeSuperBlockCell.getElementsByTagName?.('SuperBlockDiagram')?.[0]
      if (existing && existing.parentNode) {
        existing.parentNode.removeChild(existing)
      }
      if (existing) {
        activeSuperBlockCell.removeChild(existing)
      }

      // Create and append the new SuperBlockDiagram element
      const newDiagramElement = updatedDOM.documentElement // this is <SuperBlockDiagram>
      const importedElement = mainDOM.importNode(newDiagramElement, true)
      activeSuperBlockCell.appendChild(importedElement)
    }

    // Update the XML string and reflect it
    const updatedMainXML = new XMLSerializer().serializeToString(mainDOM)
    setMainDiagramBackup(updatedMainXML)
    console.log('updatedMainXML:', updatedMainXML)
    renderGalleryXML(updatedMainXML)

    // Hide the close button
    const closeBtn = document.getElementById('closeButton')
    if (closeBtn) closeBtn.style.display = 'none'
  }


  useEffect(() => {
    if (xmlData) {
      renderGalleryXML(xmlData)
    }
  }, [dispatch, xmlData])

  useEffect(() => {
    document.title = process.env.REACT_APP_DIAGRAM_NAME + ' Editor - ' + process.env.REACT_APP_NAME
    const container = gridRef.current
    const sidebar = compRef.current
    const outline = outlineRef.current
    loadGrid(container, sidebar, outline, setMainDiagramBackup, setActiveSuperBlockCell)

    if (props.location.search !== '') {
      const query = new URLSearchParams(props.location.search)
      const cktid = query.get('id')

      if (cktid.substring(0, 7) === 'gallery') {
        // Loading Gallery schematic.

        dispatch(fetchDiagram(cktid))
      } else {
        // Loading User on-cloud saved schematic.
        dispatch(fetchSchematic(cktid))
      }
    }
  }, [dispatch, props.location.search])

  return (
    <div className={classes.root}>

      <CssBaseline />

      {/* Schematic editor header, toolbar and left side pane */}
      <ComponentImages />
      <Layout header={<Header />} resToolbar={<SchematicToolbar gridRef={gridRef} mobileClose={handleDrawerToggle} />} sidebar={<ComponentSidebar compRef={compRef} />} />

      {/* Grid for drawing and designing circuits */}
      <LayoutMain>
        <div className={classes.toolbar} />
        <center>
          <button
            id="closeButton"
            onClick={handleCloseClick}
            style={{
              display: 'none',
              // position: 'absolute',
              top: '10px',
              right: '10px',
              zIndex: 1000,
              width: '24px',
              height: '24px',
              backgroundColor: '#f44336',
              color: 'white',
              fontSize: '16px',
              fontWeight: 'bold',
              border: 'none',
              borderRadius: '50%',
              cursor: 'pointer',
              lineHeight: '24px',
              textAlign: 'center',
              padding: 0
            }}
          >
            ✕
          </button>
          <div className='grid-container A4-L' ref={gridRef} id='divGrid'>
            <TailSpin
              color='#F44336'
              height={400}
              width={400}
              visible={isLoading}
            />
          </div>
        </center>
      </LayoutMain>

      {/* Schematic editor Right side pane */}
      <RightSidebar mobileOpen={mobileOpen} mobileClose={handleDrawerToggle}>
        <PropertiesSidebar gridRef={gridRef} outlineRef={outlineRef} />
      </RightSidebar>
    </div>
  )
}

SchematicEditor.propTypes = {
  location: PropTypes.object
}
