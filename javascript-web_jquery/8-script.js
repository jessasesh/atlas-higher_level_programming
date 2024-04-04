// Wait for the document to be fully loaded
$(function() {
  // URL for the API endpoint
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Perform a GET request to the API endpoint
  $.get(url, function(data) {
    // Extract the results array from the response data
    const results = data.results;
    
    // Select the UL element with ID "list_movies"
    const listMovies = $('UL#list_movies');

    // Loop through each movie in the results array
    for (let i = 0; i < results.length; i++) {
      // Extract the title of the current movie
      const movieTitle = results[i].title;
      
      // Create a new list item element with the movie title as its text content
      const listItem = $('<li>').text(movieTitle);
      
      // Append the new list item to the UL element
      listMovies.append(listItem);
    }
  });
});
