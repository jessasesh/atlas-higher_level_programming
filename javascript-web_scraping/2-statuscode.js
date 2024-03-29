#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the URL to request from command line arguments
const url = process.argv[2];

// Make a GET request to the provided URL
request.get(url, (error, response) => {
  if (error) {
    // Print the error object if an error occurred
    console.error(error);
  } else {
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
