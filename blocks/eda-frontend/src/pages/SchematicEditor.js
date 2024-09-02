// Main Layout for Schemaic Editor page.
import React, { createRef, useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { TailSpin } from 'react-loader-spinner'
import { useDispatch, useSelector } from 'react-redux'

import { CssBaseline } from '@mui/material'
import { makeStyles } from '@mui/styles'

import Layout from '../components/Shared/Layout'
import Header from '../components/SchematicEditor/Header'
import ComponentSidebar, { ComponentImages } from '../components/SchematicEditor/ComponentSidebar'
import LayoutMain from '../components/Shared/LayoutMain'
import SchematicToolbar from '../components/SchematicEditor/SchematicToolbar'
import RightSidebar from '../components/SchematicEditor/RightSidebar'
import PropertiesSidebar from '../components/SchematicEditor/PropertiesSidebar'
import LoadGrid from '../components/SchematicEditor/Helper/ComponentDrag'
import '../components/SchematicEditor/Helper/SchematicEditor.css'

import { fetchSchematic, loadGallery } from '../redux/actions/index'

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
  const compRef = createRef()
  const gridRef = createRef()
  const outlineRef = createRef()
  const dispatch = useDispatch()
  const [mobileOpen, setMobileOpen] = useState(false)
  const isLoading = useSelector(state => state.saveSchematicReducer.isLoading)

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen)
  }

  useEffect(() => {
    document.title = process.env.REACT_APP_DIAGRAM_NAME + ' Editor - ' + process.env.REACT_APP_NAME
    const container = gridRef.current
    const sidebar = compRef.current
    const outline = outlineRef.current
    LoadGrid(container, sidebar, outline)

    if (props.location.search !== '') {
      const query = new URLSearchParams(props.location.search)
      const cktid = query.get('id')

      if (cktid.substr(0, 7) === 'gallery') {
        // Loading Gallery schemaic.
        dispatch(loadGallery(cktid))
      } else {
        // Loading User on-cloud saved schemaic.
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
