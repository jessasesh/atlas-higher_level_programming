#!/usr/bin/node

// Import modules
const request = require('request');
const fs = require('fs');

// Extract URL and file path from
// command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, function (error, response, body) {
  // Write the response to specified file
  fs.writeFile(filePath, body, 'utf8', function (error) {
    if (error) {
      console.error(error);
    }
  });
});