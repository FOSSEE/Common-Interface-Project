/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import mxGraphFactory from 'mxgraph'
import { ListItem, ListItemText, Button, TextField } from '@material-ui/core'
import { TailSpin } from 'react-loader-spinner'

import { setCompProperties } from '../../redux/actions/index'
import { graph } from './Helper/ComponentDrag'
import { portSize } from './Helper/SvgParser'

const {
  mxPoint
} = new mxGraphFactory()

function getXY (portOrientation, offsetPorts, newTotalPorts, i, block) {
  let xPos
  let yPos
  let pointX
  let pointY
  let ports
  let pins
  switch (portOrientation) {
    case 'ExplicitInputPort':
      xPos = 0
      yPos = 1 - (2 * i + 1) / (2 * newTotalPorts)
      pointX = -portSize
      pointY = -portSize / 2
      ports = 'explicitInputPorts'
      pins = block.pins.explicitInputPorts
      break
    case 'ImplicitInputPort':
      xPos = 0
      yPos = 1 - (2 * (offsetPorts + i) + 1) / (2 * newTotalPorts)
      pointX = -portSize
      pointY = -portSize / 2
      ports = 'implicitInputPorts'
      pins = block.pins.implicitInputPorts
      break
    case 'ControlPort':
      xPos = (2 * i + 1) / (2 * newTotalPorts)
      yPos = 0
      pointX = -portSize / 2
      pointY = -portSize
      ports = 'controlPorts'
      pins = block.pins.controlPorts
      break
    case 'ExplicitOutputPort':
      xPos = 1
      yPos = 1 - (2 * i + 1) / (2 * newTotalPorts)
      pointX = 0
      pointY = -portSize / 2
      ports = 'explicitOutputPorts'
      pins = block.pins.explicitOutputPorts
      break
    case 'ImplicitOutputPort':
      xPos = 1
      yPos = 1 - (2 * (offsetPorts + i) + 1) / (2 * newTotalPorts)
      pointX = 0
      pointY = -portSize / 2
      ports = 'implicitOutputPorts'
      pins = block.pins.implicitOutputPorts
      break
    case 'CommandPort':
      xPos = (2 * i + 1) / (2 * newTotalPorts)
      yPos = 1
      pointX = -portSize / 2
      pointY = 0
      ports = 'commandPorts'
      pins = block.pins.commandPorts
      break
    default:
      xPos = 0
      yPos = 0
      pointX = -portSize / 2
      pointY = -portSize / 2
      ports = null
      pins = null
      break
  }
  return { xPos, yPos, pointX, pointY, ports, pins }
}

function adjustPorts (newPorts, offsetPorts, newTotalPorts, oldPorts, block, portOrientation) {
  for (let i = 0; i < Math.min(newPorts, oldPorts); i++) {
    console.log('moving port', i)
    const { xPos, yPos, pins } = getXY(portOrientation, offsetPorts, newTotalPorts, i, block)
    pins[i].geometry.x = xPos
    pins[i].geometry.y = yPos
  }
  for (let i = oldPorts; i < newPorts; i++) {
    console.log('adding port', i)
    const { xPos, yPos, pointX, pointY, ports, pins } = getXY(portOrientation, offsetPorts, newTotalPorts, i, block)
    const point = new mxPoint(pointX, pointY)
    const vp = graph.insertVertex(block, null, null, xPos, yPos, portSize, portSize, portOrientation)
    vp.geometry.relative = true
    vp.geometry.offset = point
    vp.CellType = 'Pin'
    vp.ParentComponent = block.id
    pins.push(vp)
    block[ports] += 1
  }
  if (newPorts < oldPorts) {
    const { ports, pins } = getXY(portOrientation, offsetPorts, newTotalPorts, 0, block)
    const cells = pins.slice(newPorts, oldPorts)
    graph.removeCells(cells, true)
    for (let i = oldPorts - 1; i >= newPorts; i--) {
      console.log('deleting port', i)
      pins.pop()
      block[ports] -= 1
    }
  }
}

export default function ComponentProperties () {
  // compProperties that are displayed on the right side bar when user clicks on a component on the grid.

  const compProperties = useSelector(state => state.componentPropertiesReducer.compProperties)
  const isOpen = useSelector(state => state.componentPropertiesReducer.isPropertiesWindowOpen)
  const block = useSelector(state => state.componentPropertiesReducer.block)
  const name = useSelector(state => state.componentPropertiesReducer.name)
  const parameterValues = useSelector(state => state.componentPropertiesReducer.parameter_values)
  const [val, setVal] = useState(parameterValues)
  const displayProperties = useSelector(state => state.componentPropertiesReducer.displayProperties)
  const isLoading = useSelector(state => state.componentPropertiesReducer.isLoading)

  const dispatch = useDispatch()

  useEffect(() => {
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
            console.log('changing input ports')
            adjustPorts(eiv, 0, eiv + iiv, block.explicitInputPorts, block, 'ExplicitInputPort')
            adjustPorts(iiv, eiv, eiv + iiv, block.implicitInputPorts, block, 'ImplicitInputPort')
            refreshDisplay = true
          }
        }
        if (con !== '') {
          if (con !== block.controlPorts) {
            console.log('changing control ports')
            adjustPorts(con, 0, con, block.controlPorts, block, 'ControlPort')
            refreshDisplay = true
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
            adjustPorts(eov, 0, eov + iov, block.explicitOutputPorts, block, 'ExplicitOutputPort')
            adjustPorts(iov, eov, eov + iov, block.implicitOutputPorts, block, 'ImplicitOutputPort')
            refreshDisplay = true
          }
        }
        if (com !== '') {
          if (com !== block.commandPorts) {
            console.log('changing command ports')
            adjustPorts(com, 0, com, block.commandPorts, block, 'CommandPort')
            refreshDisplay = true
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
  const link4 = 'Getting ' + name + ' Parameters'
  return (
    <div style={isOpen ? {} : { display: 'none' }}>

      <TailSpin
        color='#F44336'
        height={100}
        width={100}
        visible={isLoading}
      />

      <ListItem>
        {compProperties !== undefined ? <ListItemText primary={link1} /> : isLoading ? <ListItemText primary={link4} /> : <ListItemText primary={link3} />}
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
