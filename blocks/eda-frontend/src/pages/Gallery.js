// Main layout for gallery page.
import React, { useEffect } from 'react'
import PropTypes from 'prop-types'
import { Link as RouterLink } from 'react-router-dom'

import { Button, Card, CardActionArea, CardActions, CardContent, CardMedia, Container, CssBaseline, Grid, Typography } from '@mui/material'
import { makeStyles } from '@mui/styles'

import GallerySchSample from '../utils/GallerySchSample'

const useStyles = makeStyles((theme) => ({
  mainHead: {
    width: '100%',
    backgroundColor: '#404040',
    color: '#fff'
  },
  title: {
    fontSize: 18,
    color: '#80ff80'
  },
  header: {
    padding: theme.spacing(5, 0, 6, 0)
  },
  root: {
    display: 'flex',
    minHeight: '100vh',
    backgroundColor: '#f4f6f8'
  },
  media: {
    marginTop: theme.spacing(3),
    height: 170
  }
}))

const images = require.context('../static/gallery', true)

// Card displaying overview of gallery sample schematics.
function SchematicCard ({ sch }) {
  const classes = useStyles()

  useEffect(() => {
    document.title = 'Gallery - ' + process.env.REACT_APP_NAME
  }, [])

  const imageName = images('./' + sch.media)

  return (
    <>
      <Card>
        <CardActionArea>
          <CardMedia
            className={classes.media}
            image={imageName}
            title={sch.name}
          />
          <CardContent>
            <Typography gutterBottom variant='h5' component='h2'>
              {sch.name}
            </Typography>
            <Typography variant='body2' component='p'>
              {sch.description}
            </Typography>
          </CardContent>
        </CardActionArea>

        <CardActions>
          <Button
            target='_blank'
            component={RouterLink}
            to={'/editor?id=' + sch.save_id}
            size='small'
            color='primary'
          >
            Launch in Editor
          </Button>
        </CardActions>
      </Card>
    </>
  )
}
SchematicCard.propTypes = {
  sch: PropTypes.object
}

// Card displaying gallery page header.
function MainCard () {
  const classes = useStyles()

  const typography = process.env.REACT_APP_NAME + ' Gallery'
  const diagramTypography = 'Sample ' + process.env.REACT_APP_SMALL_DIAGRAMS_NAME + ' are listed below...'
  return (
    <Card className={classes.mainHead}>
      <CardContent>
        <Typography variant='h2' align='center' gutterBottom>
          {typography}
        </Typography>
        <Typography className={classes.title} align='center' gutterBottom>
          {diagramTypography}
        </Typography>
      </CardContent>
    </Card>
  )
}

export default function Gallery () {
  const classes = useStyles()

  return (
    <div className={classes.root}>
      <CssBaseline />
      <Container maxWidth='lg' className={classes.header}>
        <Grid
          container
          direction='row'
          justifyContent='flex-start'
          alignItems='flex-start'
          alignContent='center'
          spacing={3}
        >
          {/* Gallery Header */}
          <Grid item xs={12}>
            <MainCard />
          </Grid>

          {/* Listing Gallery Schematics */}
          {GallerySchSample.map(
            (sch) => {
              return (
                <Grid item xs={12} sm={6} lg={4} key={sch.save_id}>
                  <SchematicCard sch={sch} />
                </Grid>
              )
            }
          )}

        </Grid>
      </Container>
    </div>
  )
}
