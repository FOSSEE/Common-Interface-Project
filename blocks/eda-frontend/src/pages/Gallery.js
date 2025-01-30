// Main layout for gallery page.
import React, { useCallback, useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { Button, Card, CardActionArea, CardActions, CardContent, CardMedia, Container, CssBaseline, Grid, Typography, FormControl, InputLabel, Select, MenuItem, Input } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import { Link as RouterLink } from 'react-router-dom'
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
            component="img"
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

const BookDropdown = ({ onBookChange }) => {
  const [books, setBooks] = useState([]) // To store books from the backend
  const [selectedBook, setSelectedBook] = useState() // To store the selected book ID

  // Fetch books from the backend (optional, or use static data)
  const fetchBooks = useCallback(async () => {
    try {
      const response = await fetch('/api/save/books') // Replace with your API endpoint
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
      }
      const data = await response.json()
      setBooks(data) // Assuming the API returns an array of books
    } catch (error) {
      console.error('Error fetching books:', error)
    }
  }, [])

  useEffect(() => {
    fetchBooks()
  }, [fetchBooks])

  // Handle dropdown selection change
  const handleChange = (event) => {
    const selectedValue = event.target.value
    setSelectedBook(selectedValue)
    onBookChange(selectedValue) // Notify the parent component
  }

  return (
    <Grid container spacing={2} alignItems="center">
      <Grid item sm={6} xs={12}>
        <FormControl fullWidth>
          <InputLabel id="book-label">Book</InputLabel>
          <Select
            labelId="book-label"
            value={selectedBook}
            onChange={handleChange}
            label="Book"
          >
            {/* Option for All Books */}
            <MenuItem key="all-books" value="all">
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
      <Grid item sm={6} xs={12}>
        <FormControl fullWidth>
          <InputLabel htmlFor="search-input">Search</InputLabel>
          <Input
            id="search-input"
            type="text"
            placeholder="Search books, examples..."
          />
        </FormControl>
      </Grid>
    </Grid>
  )
}

BookDropdown.propTypes = {
  onBookChange: PropTypes.func.isRequired // This defines the expected type for the prop
}

export default function Gallery () {
  const classes = useStyles()

  // State to store the selected book ID
  const [selectedBookId, setSelectedBookId] = useState('') // Default is empty for no selection

  // Handle dropdown selection change
  const handleBookChange = (bookId) => {
    setSelectedBookId(bookId)
  }

  // Filter schematics based on the selected book ID
  const filteredSchematics =
    selectedBookId === '' // If no book is selected, show nothing
      ? []
      : selectedBookId === 'all'
        ? GallerySchSample // Show all schematics for "All Books"
        : GallerySchSample.filter((sch) => sch.book_id === parseInt(selectedBookId))

  return (
    <div className={classes.root}>
      <CssBaseline />
      <Container maxWidth="lg" className={classes.header}>
        <Grid
          container
          direction="row"
          justifyContent="flex-start"
          alignItems="flex-start"
          alignContent="center"
          spacing={3}
        >
          {/* Gallery Header */}
          <Grid item xs={12}>
            <MainCard />
          </Grid>

          {/* Book Dropdown */}
          <BookDropdown onBookChange={handleBookChange} />

          {/* Display a message or blank gallery */}
          {filteredSchematics.length === 0 ? (<Grid item xs={12}><Typography variant="h6" align="center" color="textSecondary">No schematics to display. Please select a book.</Typography></Grid>) : (filteredSchematics.map((sch) => (<Grid item xs={12} sm={6} lg={4} key={sch.save_id}><SchematicCard sch={sch} /></Grid>)))}</Grid>
      </Container>
    </div>
  )
}
