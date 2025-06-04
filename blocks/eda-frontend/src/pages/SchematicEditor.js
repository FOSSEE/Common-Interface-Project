// Main Layout for Schematic Editor page.
import React, { useEffect, useRef, useState } from 'react'
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

const useStyles = makeStyles((theme) => ({
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
    const updatedDOM = new DOMParser().parseFromString(updatedXML, 'text/xml')

    activeSuperBlockCell.SuperBlockDiagram = updatedDOM.documentElement

    const superBlockID = activeSuperBlockCell.id
    const mainDOM = new DOMParser().parseFromString(mainDiagramBackup, 'text/xml')
    const blockElem = mainDOM.querySelector(`mxCell[id="${superBlockID}"]`)

    if (blockElem) {
      const existing = blockElem.querySelector('SuperBlockDiagram')
      if (existing) existing.remove()

      const newElem = mainDOM.importNode(updatedDOM.documentElement, true)
      const wrapper = mainDOM.createElement('SuperBlockDiagram')
      wrapper.appendChild(newElem)
      blockElem.appendChild(wrapper)
    }

    const updatedMainXML = new XMLSerializer().serializeToString(mainDOM)
    setMainDiagramBackup(updatedMainXML)
    renderGalleryXML(updatedMainXML)

    // Hide the close button
    const closeBtn = document.getElementById('closeButton')
    if (closeBtn) closeBtn.style.display = 'none'
  }


  useEffect(() => {
    if (xmlData) {
      renderGalleryXML(xmlData)
    }
  }, [xmlData])

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
  }, [props.location.search])

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
