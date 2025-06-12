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

import { renderGalleryXML, getSuperblockdiagram } from '../components/SchematicEditor/Helper/ToolbarTools'
import '../components/SchematicEditor/Helper/SchematicEditor.css'
import { fetchDiagram, fetchSchematic } from '../redux/saveSchematicSlice'
import { useDispatch, useSelector } from 'react-redux'
import { styleToObject } from '../utils/GalleryUtils'
import { changePorts } from '../components/SchematicEditor/ComponentProperties'
import { graph, getCurrentDiagramXML } from '../components/SchematicEditor/Helper/ComponentDrag'

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

    const updatedXML = getCurrentDiagramXML(graph.getModel())
    console.log('updatedXML::', typeof updatedXML, updatedXML)
    const updatedDOM1 = getSuperblockdiagram(updatedXML)
    console.log('updatedDOM1:', typeof updatedDOM1, updatedDOM1)

    const xpath = "/SuperBlockDiagram/mxGraphModel/root/mxCell[@style]"
    const xpathResult = document.evaluate(
      xpath,
      updatedDOM1,
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
      const cellAttrs = cell.attributes
      const style = cellAttrs.style.value
      const defaultStyle = styleToObject(style).default
      styleCounts[defaultStyle] = (styleCounts[defaultStyle] || 0) + 1
    })
    console.log('Style counts:', styleCounts)

    const maindiagram = mainDiagramBackup
    renderGalleryXML(maindiagram)
    const blkcell = graph.getModel().getCell(activeSuperBlockCell.id)
    if (blkcell !== null) {
      blkcell.SuperBlockDiagram = updatedDOM1
      console.log('bkcell:', blkcell)
      const refreshDisplay = changePorts(
        blkcell,
        styleCounts['OUT_f'] || 0,
        styleCounts['OUTIMPL_f'] || 0,
        styleCounts['CLKOUTV_f'] || 0,
        styleCounts['IN_f'] || 0,
        styleCounts['INIMPL_f'] || 0,
        styleCounts['CLKINV_f'] || 0,
        false
      )
      if (refreshDisplay) {
        graph.refresh()
      }

      console.log('blockElem:', refreshDisplay, blkcell)

      // Hide the close button
      const closeBtn = document.getElementById('closeButton')
      if (closeBtn) closeBtn.style.display = 'none'
    }
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
