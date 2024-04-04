// Wait for the document to be fully loaded
$(document).ready(function () {
  // URL for the API endpoint
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Perform a GET request to the API endpoint
  $.get(url, function (data) {
    // Extract the "hello" property from the response data and set it as the text content of the element with ID "hello"
    $('DIV#hello').text(data.hello);
  });
});
