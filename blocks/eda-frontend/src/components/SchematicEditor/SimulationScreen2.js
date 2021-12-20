import React from 'react'
import PropTypes from 'prop-types'
import {
  AppBar,
  Button,
  Container,
  Dialog,
  Grid,
  IconButton,
  Paper,
  Slide,
  Toolbar,
  Typography
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import CloseIcon from '@material-ui/icons/Close'
import { useSelector } from 'react-redux'

import Graph2, { addPointToQueue, setStatusDone } from '../Shared/Graph2'

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

export function addPointToGraph (id, point) {
    addPointToQueue(id, point)
}

export function setGraphStatusDone () {
    setStatusDone()
}

// Screen to display simulation result in graph or text format
export default function SimulationScreen2 ({ open, close, isResult }) {
  const classes = useStyles()
  const result = useSelector(state => state.simulationReducer)
  const datapoint = useSelector(state => state.datapointReducer)
  const stitle = useSelector(state => state.netlistReducer.title)
  const graphRef = React.useRef(null);

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
            {isResult === true && datapoint.datapointId !== 0
              ? <>
                {
                  (result.graph !== {} && result.isGraph === 'true')
                    ? <Grid item xs={12} sm={12}>
                      <Paper className={classes.paper}>
                        <Typography variant='h4' align='center' gutterBottom>
                          GRAPH OUTPUT
                        </Typography>
                        <Graph2
                          ref={graphRef}
                          datapoint={datapoint}
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

SimulationScreen2.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  isResult: PropTypes.bool
}
