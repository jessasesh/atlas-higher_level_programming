#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
// Construct the API URL
const URL = 'https://swapi-api.hbtn.io/api/films/';

// Make a GET request to the Star Wars API with the specified movie ID
request.get(URL, (error, response, body) => {
  if (error) {
    // Print the error object if an error occurred
    console.error(error);
  } else {
    // Parse the JSON response body to extract the movie title
    const movieData = JSON.parse(body);
    const movieTitle = movieData.title;

    // Print the movie title
    console.log(movieTitle);
  }
});
