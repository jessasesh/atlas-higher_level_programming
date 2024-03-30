#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

// Make a GET request to the provided URL
request.get(url, function (error, response, body) {
  // Handle errors if any
  if (error) {
    console.error(error);
    return; // Exit early if an error occurs
  }

  // Parse the JSON response and extract movie data
  const movieData = JSON.parse(body).results;
  let count = 0;

  // Iterate over each movie in the movie data
  for (let i = 0; i < movieData.length; i++) {
    const characters = movieData[i].characters;

    // Iterate over each character in the movie
    for (let j = 0; j < characters.length; j++) {
      // Check if the character ID ends with '/18/' (Wedge Antilles)
      if (characters[j].endsWith('/18/')) {
        count++; // Increment the count if Wedge Antilles is present in the movie
        break; // Exit the inner loop once character ID 18 is found
      }
    }
  }

  // Print the total count of movies where Wedge Antilles is present
  console.log(count);
});
