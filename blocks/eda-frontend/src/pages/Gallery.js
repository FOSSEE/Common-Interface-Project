// Main layout for gallery page.
import { useCallback, useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { Box, Button, Card, CardActionArea, CardActions, CardContent, CardMedia, Container, CssBaseline, Grid, Typography, FormControl, InputLabel, Select, MenuItem, Input } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import api from '../utils/Api'
import { fetchGallery } from '../redux/dashboardSlice'

const images = require.context('../static/gallery', true)

// Card displaying overview of gallery sample schematics.
const SchematicCard = ({ sch }) => {
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
            image={imageName}
            title={sch.name}
            sx={{
              width: '100%',
              height: 'auto',
              objectFit: 'contain',
              mt: 3
            }}
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
  const typography = process.env.REACT_APP_NAME + ' Gallery'
  const diagramTypography = 'Sample ' + process.env.REACT_APP_SMALL_DIAGRAMS_NAME + ' are listed below...'
  return (
    <Card
      sx={{
        width: '100%',
        bgcolor: '#404040',
        color: '#fff'
      }}
    >
      <CardContent>
        <Typography variant='h2' align='center' gutterBottom>
          {typography}
        </Typography>
        <Typography
          align='center'
          gutterBottom
          sx={{
            fontSize: 18,
            color: '#80ff80'
          }}
        >
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
    return () => { setBooks([]) }
  }, [fetchBooks])

  // Handle dropdown selection change
  const handleChange = (evt) => {
    const selectedValue = evt.target.value
    setSelectedBook(selectedValue)
    onBookChange(selectedValue) // Notify the parent component
  }

  return (
    <Grid container spacing={2} alignItems='center'>
      <Grid size={12}>
        <FormControl fullWidth variant="standard">
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
      <Grid size={12}>
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
  const GallerySchSample = useSelector(state => state.dashboard.gallery)

  // State to store the selected book ID
  const [selectedBook, setSelectedBook] = useState('')
  const [searchTerm, setSearchTerm] = useState('')

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(fetchGallery())
  }, [dispatch])

  // Handle dropdown selection change
  const handleBookChange = (book) => {
    setSelectedBook(book)
  }

  // Handle search term change
  const handleSearch = (term) => {
    setSearchTerm(term)
  }

  const filteredSchematics =
    (() => {
      if (!selectedBook) return []
      if (selectedBook === 'all') return GallerySchSample
      const selectedBookId = Number(selectedBook)
      return GallerySchSample.filter((sch) => sch.book_id === selectedBookId)
    })()

  const NOBLOCK = /^no./
  const SCE = /^(sce|sci|script)/
  const NOSCE = /^no(sce|sci|script)/
  const terms = searchTerm.trim().toLowerCase().split(/\s+/).filter(Boolean)

  // Then, filter based on the search term (independent from book selection)
  const finalfilteredSchematics =
    terms.length === 0
      ? filteredSchematics
      : filteredSchematics.filter((sch) => {
        return terms.every((st) =>
          sch.lcname.includes(st) ||
          sch.lcdescription.includes(st) ||
          (!NOBLOCK.test(st) && (';' + sch.blocks).includes(';' + st)) ||
          (NOBLOCK.test(st) && !(';' + sch.blocks + ';').includes(';' + st.substring(2) + ';')) ||
          sch.save_id.startsWith('gallery' + st) ||
          (SCE.test(st) && sch.has_script) ||
          (NOSCE.test(st) && !sch.has_script)
        )
      })

  return (
    <Box
      component='div'
      sx={{
        display: 'flex',
        minHeight: '100vh',
        bgcolor: '#f4f6f8'
      }}
    >
      <CssBaseline />
      <Container
        maxWidth='lg'
        sx={{
          pt: 5,
          pb: 6
        }}
      >
        <Grid container direction='row' justifyContent='flex-start' alignItems='flex-start' alignContent='center' spacing={3}>
          {/* Gallery Header */}
          <Grid size={12}>
            <MainCard />
          </Grid>

          {/* BookDropdown */}
          <Grid size={6}>
            <BookDropdown onBookChange={handleBookChange} />
          </Grid>

          {/* SearchComponent */}
          <Grid size={6}>
            <SearchComponent onSearch={handleSearch} />
          </Grid>

          {/* Display a message or blank gallery */}
          <Grid size={12}>
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
              <Grid size={4} key={sch.save_id}>
                <SchematicCard sch={sch} />
              </Grid>
            ))
          }
        </Grid>
      </Container>
    </Box>
  )
}

export default Gallery
