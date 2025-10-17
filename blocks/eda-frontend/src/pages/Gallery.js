// Main layout for gallery page.
import { useCallback, useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link as RouterLink } from 'react-router-dom'

import PropTypes from 'prop-types'

import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import ButtonGroup from '@mui/material/ButtonGroup'
import Card from '@mui/material/Card'
import CardActionArea from '@mui/material/CardActionArea'
import CardActions from '@mui/material/CardActions'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Container from '@mui/material/Container'
import CssBaseline from '@mui/material/CssBaseline'
import FormControl from '@mui/material/FormControl'
import Grid from '@mui/material/Grid'
import Input from '@mui/material/Input'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import Select from '@mui/material/Select'
import Typography from '@mui/material/Typography'

import { fetchGallery } from '../redux/dashboardSlice'
import api from '../utils/Api'

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
              objectFit: 'contain',
              mt: 3,
              height: 'auto'
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
        <FormControl variant='standard' fullWidth>
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

  useEffect(() => {
    const timeout = setTimeout(() => {
      onSearch(searchTerm)
    }, 300)

    return () => {
      clearTimeout(timeout)
    }
  }, [searchTerm, onSearch])

  const handleSearch = (event) => {
    const value = event.target.value.trimStart()
    setSearchTerm(value)
  }

  return (
    <Grid container spacing={2}>
      <Grid size={12}>
        <FormControl variant='standard' fullWidth>
          <InputLabel htmlFor='search-input'>Search</InputLabel>
          <Input
            id='search-input'
            type='text'
            placeholder='Search blocks, examples...'
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

  const ITEMS_PER_PAGE = parseInt(process.env.REACT_APP_ITEMS_PER_PAGE || '12', 10)
  const [page, setPage] = useState(1)

  useEffect(() => {
    setPage(1)
  }, [searchTerm, selectedBook])

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

  const totalPages = Math.ceil(finalfilteredSchematics.length / ITEMS_PER_PAGE)

  const paginatedSchematics = finalfilteredSchematics.slice(
    (page - 1) * ITEMS_PER_PAGE,
    page * ITEMS_PER_PAGE
  )

  const renderPagination = () => {
    if (totalPages <= 1) return null

    const visiblePages = 5
    let startPage = Math.max(1, page - 2)
    const endPage = Math.min(totalPages, startPage + visiblePages - 1)

    if (endPage - startPage < visiblePages - 1) {
      startPage = Math.max(1, endPage - visiblePages + 1)
    }

    const pages = []
    for (let i = startPage; i <= endPage; i++) {
      pages.push(i)
    }

    return (
      <Grid container justifyContent='center' style={{ marginTop: '1rem' }}>
        <ButtonGroup variant="outlined" color="primary">
          <Button onClick={() => setPage(1)} disabled={page === 1}>{'«'}</Button>
          <Button onClick={() => setPage(page - 1)} disabled={page === 1}>{'‹'}</Button>

          {pages.map(p => (
            <Button
              key={p}
              onClick={() => setPage(p)}
              variant={p === page ? 'contained' : 'outlined'}
              color={p === page ? 'primary' : 'default'}
            >
              {p}
            </Button>
          ))}

          <Button onClick={() => setPage(page + 1)} disabled={page === totalPages}>{'›'}</Button>
          <Button onClick={() => setPage(totalPages)} disabled={page === totalPages}>{'»'}</Button>
        </ButtonGroup>
      </Grid>
    )
  }

  return (
    <Box
      component='div'
      sx={{
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
        bgcolor: '#f4f6f8'
      }}
    >
      <CssBaseline />
      <Container
        maxWidth={false}
        sx={{
          pt: 5,
          pb: 15
        }}
      >
        <Grid container direction='row' justifyContent='flex-start' alignItems='flex-start' alignContent='center' spacing={3}>
          {/* Gallery Header */}
          <Grid size={12}>
            <MainCard />
          </Grid>

          <Grid size={12}>
            <Grid container spacing={2}>
              {/* BookDropdown */}
              <Grid size={{ xs: 12, md: 6 }}>
                <BookDropdown onBookChange={handleBookChange} />
              </Grid>

              {/* SearchComponent */}
              <Grid size={{ xs: 12, md: 6 }}>
                <SearchComponent onSearch={handleSearch} />
              </Grid>
            </Grid>
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
            paginatedSchematics.map((sch) => (
              <Grid size={{ xs: 12, md: 6, lg: 4, xl: 3 }} key={sch.save_id}>
                <SchematicCard sch={sch} />
              </Grid>
            ))
          }

        </Grid>
      </Container>
      <BackToTopButton />
      <div
        style={{
          position: 'fixed',
          bottom: '1rem',
          right: '1.75rem',
          zIndex: 1100
        }}
      >
        {renderPagination()}
      </div>
    </Box>
  )
}

const BackToTopButton = () => {
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const toggleVisibility = () => {
      setVisible(window.pageYOffset > 100)
    }

    window.addEventListener('scroll', toggleVisibility)
    return () => window.removeEventListener('scroll', toggleVisibility)
  }, [])

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  return visible ? (
    <div
      onClick={scrollToTop}
      style={{
        position: 'fixed',
        bottom: '60px',
        right: '40px',
        zIndex: 1000,
        backgroundColor: '#3650c9',
        color: 'white',
        border: 'none',
        padding: '5px 8px',
        borderRadius: '8px',
        fontSize: '28px',
        cursor: 'pointer',
        opacity: 0.9
      }}
    >
      ↑
    </div>
  ) : null
}

export default Gallery
