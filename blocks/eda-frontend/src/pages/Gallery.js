// Main layout for gallery page.
import React, { useCallback, useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { Button, Card, CardActionArea, CardActions, CardContent, CardMedia, Container, CssBaseline, Grid, Typography, FormControl, InputLabel, Select, MenuItem, Input } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import { Link as RouterLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import api from '../utils/Api'
import { fetchGallery } from '../redux/actions/index'

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
const SchematicCard = ({ sch }) => {
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
            component='img'
            className={classes.media}
            image={imageName}
            title={sch.name}
            style={{ width: '100%', height: 'auto', objectFit: 'contain' }}
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
const MainCard = () => {
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

const BookDropdown = ({ onBookChange }) => {
  const [books, setBooks] = useState([]) // To store books from the backend
  const [selectedBook, setSelectedBook] = useState('')

  // Fetch books from the backend (optional, or use static data)
  const fetchBooks = useCallback(() => {
    api.get('save/books')
      .then((res) => {
        if (res.status !== 200) {
          throw new Error(`HTTP error! Status: ${res.status}`)
        }
        setBooks(res.data) // Assuming the API returns an array of books
      })
      .catch(err => { console.error('Error fetching books:', err) })
  }, [])

  useEffect(() => {
    fetchBooks()
  }, [fetchBooks])

  // Handle dropdown selection change
  const handleChange = (evt) => {
    const selectedValue = evt.target.value
    setSelectedBook(selectedValue)
    onBookChange(selectedValue) // Notify the parent component
  }

  return (
    <Grid container spacing={2} alignItems='center'>
      <Grid item xs={12}>
        <FormControl fullWidth>
          <InputLabel id='book-label'>Book</InputLabel>
          <Select
            labelId='book-label'
            value={selectedBook || ''}
            onChange={handleChange}
            label='Book'
          >
            <MenuItem key='all-books' value='all'>
              All Books ({books?.reduce((total, book) => total + (book.example_count || 0), 0)})
            </MenuItem>
            {/* Render dynamic book options */}
            {books?.map((book) => (
              <MenuItem key={`book-${book.id}`} value={book.id}>
                {book.book_name} ({book.author_name}) ({book.example_count || 0})
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
    </Grid>
  )
}

BookDropdown.propTypes = {
  onBookChange: PropTypes.func.isRequired
}

const SearchComponent = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('')

  const handleSearch = (event) => {
    const value = event.target.value.trimStart()
    setSearchTerm(value)
    onSearch(value)
  }

  return (
    <Grid container spacing={2}>
      <Grid item xs={12}>
        <FormControl fullWidth>
          <InputLabel htmlFor='search-input'>Search</InputLabel>
          <Input
            id='search-input'
            type='text'
            placeholder='Search books, examples...'
            value={searchTerm}
            onChange={handleSearch}
          />
        </FormControl>
      </Grid>
    </Grid>
  )
}

SearchComponent.propTypes = {
  onSearch: PropTypes.func.isRequired
}

const Gallery = () => {
  const classes = useStyles()
  const GallerySchSample = useSelector(state => state.dashboardReducer.gallery)

  // State to store the selected book ID
  const [selectedBook, setSelectedBook] = useState('')
  const [searchTerm, setSearchTerm] = useState('')

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(fetchGallery())
  }, [])

  // Handle dropdown selection change
  const handleBookChange = (book) => {
    setSelectedBook(book)
  }

  // Handle search term change
  const handleSearch = (term) => {
    setSearchTerm(term)
  }

  const filteredSchematics =
    // Filter based on selected book ID first
    selectedBook === '' // If no book is selected, show nothing
      ? []
      : selectedBook === 'all'
        ? GallerySchSample // Show all schematics for 'All Books'
        : GallerySchSample.filter((sch) => sch.book_id === parseInt(selectedBook))

  const st = searchTerm.trim().toLowerCase()
  const galleryst = 'gallery' + st

  // Then, filter based on the search term (independent from book selection)
  const finalfilteredSchematics =
    st === ''
      ? filteredSchematics
      : filteredSchematics.filter((sch) => {
        return (
          sch.lcname.includes(st) ||
          sch.lcdescription.includes(st) ||
          sch.save_id.startsWith(galleryst)
        )
      })

  return (
    <div className={classes.root}>
      <CssBaseline />
      <Container maxWidth='lg' className={classes.header}>
        <Grid container direction='row' justifyContent='flex-start' alignItems='flex-start' alignContent='center' spacing={3}>
          {/* Gallery Header */}
          <Grid item xs={12}>
            <MainCard />
          </Grid>

          <Grid item xs={12}>
            <Grid container spacing={2}>
              {/* BookDropdown */}
              <Grid item xs={12} md={6}>
                <BookDropdown onBookChange={handleBookChange} />
              </Grid>

              {/* SearchComponent */}
              <Grid item xs={12} md={6}>
                <SearchComponent onSearch={handleSearch} />
              </Grid>
            </Grid>
          </Grid>

          {/* Display a message or blank gallery */}
          <Grid item xs={12}>
            <Typography variant='h6' align='center' color='textSecondary'>
              {
                finalfilteredSchematics.length === 0
                  ? `No ${process.env.REACT_APP_SMALL_DIAGRAMS_NAME} to display. ${selectedBook === ''
                    ? 'Please select a book.'
                    : selectedBook === 'all'
                      ? 'Please try another search term.'
                      : 'Please select another book or try another search term.'
                  }`
                  : `${finalfilteredSchematics.length} ${finalfilteredSchematics.length !== 1
                    ? `${process.env.REACT_APP_SMALL_DIAGRAMS_NAME}`
                    : `${process.env.REACT_APP_SMALL_DIAGRAM_NAME}`}`
              }
            </Typography>
          </Grid>

          {
            finalfilteredSchematics.map((sch) => (
              <Grid item xs={12} sm={6} lg={4} key={sch.save_id}>
                <SchematicCard sch={sch} />
              </Grid>
            ))
          }
        </Grid>
      </Container>
    </div>
  )
}

export default Gallery
