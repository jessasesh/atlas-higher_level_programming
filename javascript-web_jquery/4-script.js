// Wait for the document to fully load
$(document).ready(function () {
  // Select the DIV#toggle_header element
  const toggleHeader = $('div#toggle_header');

  // Check if the toggleHeader element exists
  if (!toggleHeader.length) {
    console.error('Error: The "toggle_header" element does not exist.');
  } else {
    // Attach a click event listener to the toggleHeader element
    toggleHeader.on('click', function () {
      // Select the header
      const header = $('header');

      // Toggle between the red and green classes
      headerElement.toggleClass('green');
      headerElement.toggleClass('red');
    });
  }
});
