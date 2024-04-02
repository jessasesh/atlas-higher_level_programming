// Wait for the document to fully load
$(document).ready(function () {
  // Select the element with id "red_header"
  const redHeader = $('#red_header');

  // Check if the redHeader element exists
  if (!redHeader.length) {
    // Log an error message to the console if redHeader is not found
    console.error('Error: The "red_header" element does not exist.');
  } else {
    // Attach a click event listener to the redHeader element
    redHeader.on('click', function () {
      // Update the text color of the header to red when redHeader is clicked
      redHeader.css('color', '#FF0000');
    });
  }
});