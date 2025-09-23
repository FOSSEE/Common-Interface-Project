import PropTypes from 'prop-types'

import Box from '@mui/material/Box'

// Display main content of layout
export default function LayoutMain ({ children }) {
  return (
    <>
      <Box
        component='main'
        sx={{
          flexGrow: 1,
          px: 3,
          py: 5,
          bgcolor: '#f4f6f8',
          height: '100vh',
          overflow: 'auto'
        }}
      >
        {children}
      </Box>
    </>
  )
}

LayoutMain.propTypes = {
  children: PropTypes.array.isRequired
}
