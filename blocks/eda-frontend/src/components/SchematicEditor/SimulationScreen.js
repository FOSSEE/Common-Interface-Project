import React from 'react'
import PropTypes from 'prop-types'
import {
  AppBar,
  Button,
  Container,
  Dialog,
  Grid,
  IconButton,
  TextField,
  Paper,
  Slide,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Toolbar,
  Typography
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import CloseIcon from '@material-ui/icons/Close'
import { useSelector } from 'react-redux'

import Graph from '../Shared/Graph'

const Transition = React.forwardRef(function Transition (props, ref) {
  return <Slide direction='up' ref={ref} {...props} />
})

const useStyles = makeStyles((theme) => ({
  appBar: {
    position: 'relative'
  },
  title: {
    marginLeft: theme.spacing(2),
    flex: 1
  },
  header: {
    padding: theme.spacing(5, 0, 6),
    color: '#fff'
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: '#404040',
    color: '#fff'
  }
}))

// Screen to display simulation result in graph or text format
export default function SimulationScreen ({ open, close, isResult }) {
  const classes = useStyles()
  const result = useSelector(state => state.simulationReducer)
  const stitle = useSelector(state => state.netlistReducer.title)
  const [xscale, setXScale] = React.useState('si')
  const [yscale, setYScale] = React.useState('si')
  const [precision, setPrecision] = React.useState(5)
  const precisionArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  const scales = {
    G: 1000000000,
    M: 1000000,
    K: 1000,
    si: 1,
    m: 0.001,
    u: 0.000001,
    n: 0.000000001,
    p: 0.000000000001
  }
  const handleXScale = (evt) => {
    setXScale(evt.target.value)
  }

  const handleYScale = (evt) => {
    setYScale(evt.target.value)
  }
  const handlePrecision = (evt) => {
    setPrecision(evt.target.value)
  }

  const typography1 = 'SOMETHING WENT WRONG. Please Check The Simulation Parameters.'
  const typography2 = 'SOMETHING WENT WRONG. Please Check The Simulation Parameters And ' + process.env.REACT_APP_DIAGRAM_NAME + '.'
  return (
    <div>
      <Dialog
        fullScreen open={open} onClose={close} TransitionComponent={Transition} PaperProps={{
          style: {
            backgroundColor: '#4d4d4d',
            boxShadow: 'none'
          }
        }}
      >
        <AppBar position='static' elevation={0} className={classes.appBar}>
          <Toolbar variant='dense' style={{ backgroundColor: '#404040' }}>
            <IconButton edge='start' color='inherit' onClick={close} aria-label='close'>
              <CloseIcon />
            </IconButton>
            <Typography variant='h6' className={classes.title}>
              Simulation Result
            </Typography>
            <Button autoFocus color='inherit' onClick={close}>
              close
            </Button>
          </Toolbar>
        </AppBar>
        <Container maxWidth='lg' className={classes.header}>
          <Grid
            container
            spacing={3}
            direction='row'
            justify='center'
            alignItems='center'
          >
            {/* Card to display simulation result screen header */}
            <Grid item xs={12} sm={12}>
              <Paper className={classes.paper}>
                <Typography variant='h2' align='center' gutterBottom>
                  {result.title}
                </Typography>
                <Typography variant='h5' align='center' component='p' gutterBottom>
                  Simulation Result for {stitle} *
                </Typography>
              </Paper>
            </Grid>

            {/* Display graph result */}
            {isResult === true
              ? <>
                {
                  (result.graph !== {} && result.isGraph === 'true')
                    ? <Grid item xs={12} sm={12}>
                      <Paper className={classes.paper}>
                        <Typography variant='h4' align='center' gutterBottom>
                          GRAPH OUTPUT
                        </Typography>
                        <div style={{ padding: '15px 10px 10px 10px', margin: '20px 0px', backgroundColor: 'white', borderRadius: '5px' }}>
                          <TextField
                            style={{ width: '20%' }}
                            id='xscale'
                            size='small'
                            variant='outlined'
                            select
                            label='Select X Axis Scale'
                            value={xscale}
                            onChange={handleXScale}
                            SelectProps={{
                              native: true
                            }}
                          >
                            <option value='G'>
                              Giga (G)
                            </option>
                            <option value='M'>
                              Mega (MEG)
                            </option>
                            <option value='K'>
                              Kilo (K)
                            </option>
                            <option value='si'>
                              SI UNIT
                            </option>

                            <option value='m'>
                              Milli (m)
                            </option>
                            <option value='u'>
                              Micro (u)
                            </option>
                            <option value='n'>
                              Nano (n)
                            </option>
                            <option value='p'>
                              Pico (p)
                            </option>

                          </TextField>
                          <TextField
                            style={{ width: '20%', marginLeft: '10px' }}
                            id='yscale'
                            size='small'
                            variant='outlined'
                            select
                            label='Select Y Axis Scale'
                            value={yscale}
                            onChange={handleYScale}
                            SelectProps={{
                              native: true
                            }}
                          >
                            <option value='G'>
                              Giga (G)
                            </option>
                            <option value='M'>
                              Mega (MEG)
                            </option>
                            <option value='K'>
                              Kilo (K)
                            </option>
                            <option value='si'>
                              SI UNIT
                            </option>

                            <option value='m'>
                              Milli (m)
                            </option>
                            <option value='u'>
                              Micro (u)
                            </option>
                            <option value='n'>
                              Nano (n)
                            </option>
                            <option value='p'>
                              Pico (p)
                            </option>

                          </TextField>

                          <TextField
                            style={{ width: '20%', marginLeft: '10px' }}
                            id='precision'
                            size='small'
                            variant='outlined'
                            select
                            label='Select Precision'
                            value={precision}
                            onChange={handlePrecision}
                            SelectProps={{
                              native: true
                            }}
                          >
                            {
                              precisionArr.map((d, i) => {
                                return (
                                  <option key={i} value={d}>
                                    {d}
                                  </option>
                                )
                              })
                            }

                          </TextField>
                        </div>
                        <Graph
                          labels={result.graph.labels}
                          x={result.graph.x_points}
                          y={result.graph.y_points}
                          xscale={xscale}
                          yscale={yscale}
                          precision={precision}
                        />
                      </Paper>
                    </Grid>
                    : (result.isGraph === 'true') ? <span>{typography1}</span> : <span />
                }

                {/* Display text result */}
                {
                  (result.isGraph === 'false')
                    ? <Grid item xs={12} sm={12}>
                      <Paper className={classes.paper}>
                        <Typography variant='h4' align='center' gutterBottom>
                          OUTPUT
                        </Typography>
                        <div style={{ padding: '15px 10px 10px 10px', backgroundColor: 'white', margin: '20px 0px', borderRadius: '5px' }}>
                          <TextField
                            style={{ width: '20%' }}
                            id='xscale'
                            size='small'
                            variant='outlined'
                            select
                            label='Select Scale'
                            value={xscale}
                            onChange={handleXScale}
                            SelectProps={{
                              native: true
                            }}
                          >
                            <option value='G'>
                              Giga (G)
                            </option>
                            <option value='M'>
                              Mega (MEG)
                            </option>
                            <option value='K'>
                              Kilo (K)
                            </option>
                            <option value='si'>
                              SI UNIT
                            </option>

                            <option value='m'>
                              Milli (m)
                            </option>
                            <option value='u'>
                              Micro (u)
                            </option>
                            <option value='n'>
                              Nano (n)
                            </option>
                            <option value='p'>
                              Pico (p)
                            </option>

                          </TextField>

                          <TextField
                            style={{ width: '20%', marginLeft: '10px' }}
                            id='precision'
                            size='small'
                            variant='outlined'
                            select
                            label='Select Precision'
                            value={precision}
                            onChange={handlePrecision}
                            SelectProps={{
                              native: true
                            }}
                          >
                            {
                              precisionArr.map((d, i) => {
                                return (
                                  <option key={i} value={d}>
                                    {d}
                                  </option>
                                )
                              })
                            }

                          </TextField>
                        </div>

                        <TableContainer component={Paper}>
                          <Table className={classes.table} aria-label='simple table'>
                            <TableHead>
                              <TableRow>
                                <TableCell align='center'>Node/Branch</TableCell>
                                <TableCell align='center'>Value</TableCell>
                                <TableCell align='center'>Unit</TableCell>
                              </TableRow>
                            </TableHead>
                            <TableBody>
                              {result.text.map((line, index) => (
                                <TableRow key={index}>
                                  <TableCell align='center'>{line.split('=')[0]}</TableCell>
                                  <TableCell align='center'>{(parseFloat(line.split(' ')[2]) / scales[xscale]).toFixed(precision)}</TableCell>
                                  <TableCell align='center'>{xscale === 'si' ? '' : xscale}{line.split(' ')[3]}</TableCell>
                                </TableRow>
                              ))}

                            </TableBody>
                          </Table>
                        </TableContainer>

                      </Paper>
                    </Grid>
                    : <span />
                }
              </>
              : <Grid item xs={12} sm={12}>
                <Paper className={classes.paper}>
                  <Typography variant='h6' align='center' gutterBottom>
                    {typography2} {/* Error handling message in case of null result */}
                  </Typography>
                </Paper>
              </Grid>
            }
          </Grid>
        </Container>
      </Dialog>
    </div>
  )
}

SimulationScreen.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  isResult: PropTypes.bool
}
