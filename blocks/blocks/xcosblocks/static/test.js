const sse = new EventSource('/api/instructions/get', { withCredentials: true })
sse.addEventListener('instruction', e => {
  const data = e.data
  console.log('instruction', data)
})
sse.addEventListener('done', e => {
  console.log('done')
  sse.close()
})
