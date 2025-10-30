const BuildInfo = () => {
  const gitCommit = process.env.REACT_APP_GIT_COMMIT || 'unknown'
  const buildDate = process.env.REACT_APP_BUILD_DATE || 'unknown'

  return (
    <div style={{ fontSize: '0.8rem', color: '#666', marginTop: '1rem' }}>
      Build: {gitCommit} ({buildDate})
    </div>
  )
}

export default BuildInfo
