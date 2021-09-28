
export default function textToFile (data) {
  // create a file from a blob

  const myblob = new Blob([data], {
    type: 'text/plain'
  })
  const file = new File([myblob], 'netlist.cir', { type: 'text/plain', lastModified: Date.now() })
  return file
}
