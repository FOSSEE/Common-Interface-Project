import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { setCompProperties } from '../../redux/actions/index'
import { ListItem, ListItemText, Button, TextField } from '@material-ui/core'

export default function ComponentProperties () {
  // compProperties that are displayed on the right side bar when user clicks on a component on the grid.

  const compProperties = useSelector(state => state.componentPropertiesReducer.compProperties)
  const isOpen = useSelector(state => state.componentPropertiesReducer.isPropertiesWindowOpen)
  const id = useSelector(state => state.componentPropertiesReducer.id)
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

  const link1 = process.env.REACT_APP_BLOCK_NAME + ' Parameters';
  const link2 = 'Set ' + process.env.REACT_APP_BLOCK_NAME + ' Parameters';
  return (

    <div style={isOpen ? {} : { display: 'none' }}>

      <ListItem>
        <ListItemText primary={link1} />
      </ListItem>

      {
        Object.keys(val).map((keyName, i) => {
          if (keyName.match(/^p[0-9]*_value$/)) {
            let rootKeyName = keyName.substr(0, 4)
            if (compProperties[rootKeyName] !== null) {
              return <ListItem key={i}>
                <TextField id={keyName} label={compProperties[rootKeyName]} value={val[keyName] || ''} size='small' variant='outlined' onChange={getInputValues} />
              </ListItem>
            }
          }

          return ''
        })
      }

      <ListItem>
        <Button size='small' variant="contained" color="primary" onClick={setProps}>{link2}</Button>
      </ListItem>

    </div>
  )
}
