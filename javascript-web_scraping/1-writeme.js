#!/usr/bin/node

/* Import File System module */
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Get the string to write from command line arguments
const toWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, toWrite, 'utf8', function (error) {
  // Check if an error occurred during writing
  if (error) {
    // Print the error object if an error occurred
    console.error(error);
  }
});
