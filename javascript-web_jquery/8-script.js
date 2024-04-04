$(function() {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  $.get(url, function(data) {
    const results = data.results;
    const listMovies = $('UL#list_movies');

    for (let i = 0; i < results.length; i++) {
      const movieTitle = results[i].title;
      const listItem = $('<li>').text(movieTitle);
      listMovies.append(listItem);
    }
  });
});
