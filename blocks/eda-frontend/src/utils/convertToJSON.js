const fs = require('fs'); // Import the filesystem module
const path = require('path');

// Import the GallerySchSample file
const GallerySchSample = require('./GallerySchSample.js');

// Convert the data to JSON
const outputPath = path.join(__dirname, 'GallerySchSample.json');
fs.writeFileSync(outputPath, JSON.stringify(GallerySchSample, null, 2));

console.log(`Data has been successfully converted to ${outputPath}`);
