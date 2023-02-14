/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import React, { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import mxGraphFactory from 'mxgraph'
import { ListItem, ListItemText, Button, TextField } from '@material-ui/core'

import { setCompProperties } from '../../redux/actions/index'
import { graph } from './Helper/ComponentDrag'
import { portSize } from './Helper/SvgParser'

const {
  mxPoint
} = new mxGraphFactory()

export default function ComponentProperties () {
  // compProperties that are displayed on the right side bar when user clicks on a component on the grid.

  const compProperties = useSelector(state => state.componentPropertiesReducer.compProperties)
  const isOpen = useSelector(state => state.componentPropertiesReducer.isPropertiesWindowOpen)
  const block = useSelector(state => state.componentPropertiesReducer.block)
  const name = useSelector(state => state.componentPropertiesReducer.name)
  const parameterValues = useSelector(state => state.componentPropertiesReducer.parameter_values)
  const [val, setVal] = useState(parameterValues)
  const displayProperties = useSelector(state => state.componentPropertiesReducer.displayProperties)

  const dispatch = useDispatch()

  React.useEffect(() => {
    setVal(parameterValues)
    let refreshDisplay = false
    if (block != null && displayProperties != null) {
      const dp = displayProperties.display_parameter
      if (dp != null && dp !== '') {
        block.displayProperties = {
          display_parameter: dp
        }
        refreshDisplay = true
      }
      // make the component images smaller by scaling
      if (Array.isArray(displayProperties.ports)) {
        let [eiv, iiv, con, eov, iov, com] = displayProperties.ports
        if (eiv !== '' || iiv !== '') {
          if (eiv === '') {
            eiv = block.explicitInputPorts
          }
          if (iiv === '') {
            iiv = block.implicitInputPorts
          }
          if (eiv !== block.explicitInputPorts || iiv !== block.implicitInputPorts) {
            const pointX = -portSize
            const pointY = -portSize / 2
            const portOrientation = 'ExplicitInputPort'
            const pins = block.pins.explicitInputPorts
            for (let i = 0; i < Math.min(eiv, block.explicitInputPorts); i++) {
              const xPos = 0
              const yPos = 1 - (2 * i + 1) / (2 * (eiv + iiv))
              pins[i].geometry.x = xPos
              pins[i].geometry.y = yPos
            }
            for (let i = block.explicitInputPorts; i < eiv; i++) {
              const xPos = 0
              const yPos = 1 - (2 * i + 1) / (2 * (eiv + iiv))
              const point = new mxPoint(pointX, pointY)
              const vp = graph.insertVertex(block, null, null, xPos, yPos, portSize, portSize, portOrientation)
              vp.geometry.relative = true
              vp.geometry.offset = point
              vp.CellType = 'Pin'
              vp.ParentComponent = block.id
              pins.push(vp)
            }
            if (eiv < block.explicitInputPorts) {
              const cells = pins.slice(eiv, block.explicitInputPorts)
              graph.removeCells(cells, true)
              for (let i = block.explicitInputPorts - 1; i >= eiv; i--) {
                pins.pop()
              }
            }
            block.explicitInputPorts = eiv
            for (let i = 0; i < Math.min(iiv, block.implicitInputPorts); i++) {
              console.log('moving input port', eiv + i)
            }
            for (let i = block.implicitInputPorts; i < iiv; i++) {
              console.log('adding input port', eiv + i)
            }
            for (let i = iiv; i < block.implicitInputPorts; i++) {
              console.log('deleting input port', eiv + i)
            }
            refreshDisplay = true
          }
        }
        if (con !== '') {
          if (con !== block.controlPorts) {
            console.log('changing control ports')
          }
        }
        if (eov !== '' || iov !== '') {
          if (eov === '') {
            eov = block.explicitOutputPorts
          }
          if (iov === '') {
            iov = block.implicitOutputPorts
          }
          if (eov !== block.explicitOutputPorts || iov !== block.implicitOutputPorts) {
            console.log('changing output ports')
          }
        }
        if (com !== '') {
          if (com !== block.commandPorts) {
            console.log('changing command ports')
          }
        }
      }
      if (refreshDisplay) {
        graph.refresh()
      }
    }
  }, [parameterValues, displayProperties])

  const getInputValues = (evt) => {
    const value = evt.target.value
    setVal({
      ...val,
      [evt.target.id]: value
    })
  }

  const setProps = () => {
    dispatch(setCompProperties(block, val))
  }

  const link1 = name + ' Parameters'
  const link2 = 'Set ' + process.env.REACT_APP_BLOCK_NAME + ' Parameters'
  const link3 = 'No ' + name + ' Parameters'
  return (
    <div style={isOpen ? {} : { display: 'none' }}>

      <ListItem>
        {compProperties !== undefined ? <ListItemText primary={link1} /> : <ListItemText primary={link3} />}
      </ListItem>

      {
        Object.keys(val).map((keyName, i) => {
          if (keyName.match(/^p[0-9]*_value$/)) {
            const rootKeyName = keyName.substr(0, 4)
            const typeId = rootKeyName + '_type'
            if (compProperties !== undefined && compProperties[rootKeyName] !== null && compProperties[typeId] !== null) {
              return (
                <ListItem key={i}>
                  <TextField id={keyName} label={compProperties[rootKeyName]} value={val[keyName] || ''} size='small' variant='outlined' onChange={getInputValues} />
                </ListItem>
              )
            }
          }

          return ''
        })
      }

      {
        compProperties !== undefined && <ListItem>
          <Button size='small' variant='contained' color='primary' onClick={setProps}>{link2}</Button>
        </ListItem>
      }

    </div>
  )
}
