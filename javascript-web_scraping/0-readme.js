#!/usr/bin/node

// Import the 'fs' module to work with files
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the content of the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred
  } else {
    console.log(data); // Print the content of the file
  }
});
