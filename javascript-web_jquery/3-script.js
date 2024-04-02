// Wait for the document to fully load
$(document).ready(function () {
  // Select the DIV#red_header element
  const redHeader = $('div#red_header');

  // Attach a click event listener to the redHeader element
  redHeader.on('click', function () {
    // Select the <header> element
    const header = $('header');

    // Add the class 'red' to the <header> element
    header.addClass('red');
  });
});
