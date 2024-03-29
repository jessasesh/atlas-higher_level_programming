#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
// Construct the API URL
const URL = 'https://swapi-api.hbtn.io/api/films/';

// Make a GET request to the Star Wars API with the specified movie ID
request.get(URL + movieId, function (error, response, body) {
  if (error) {
    // Print the error
    console.error(error);
  } else {
    // Parse the JSON response to extract the movie title
    const movieData = JSON.parse(body);
    // Print movie title
    console.log(movieData.title);
  }
});
