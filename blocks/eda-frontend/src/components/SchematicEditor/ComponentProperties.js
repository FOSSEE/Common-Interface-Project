import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { setCompProperties } from '../../redux/actions/index'
import { ListItem, ListItemText, Button, TextField } from '@material-ui/core'

export default function ComponentProperties () {
  // compProperties that are displayed on the right side bar when user clicks on a component on the grid.

  const compProperties = useSelector(state => state.componentPropertiesReducer.compProperties)
  const isOpen = useSelector(state => state.componentPropertiesReducer.isPropertiesWindowOpen)
  const id = useSelector(state => state.componentPropertiesReducer.id)
  const name = useSelector(state => state.componentPropertiesReducer.name)
  const parameter_values = useSelector(state => state.componentPropertiesReducer.parameter_values)
  const [val, setVal] = useState(parameter_values)

  const dispatch = useDispatch()

  useEffect(() => {
    setVal(parameter_values)
  }, [parameter_values])

  const getInputValues = (evt) => {
    const value = evt.target.value
    setVal({
      ...val,
      [evt.target.id]: value
    })
  }

  const setProps = () => {
    dispatch(setCompProperties(id, val))
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
            const type_id = rootKeyName + '_type'
            if (compProperties !== undefined && compProperties[rootKeyName] !== null && compProperties[type_id] !== null) {
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
