// Select the header element using jQuery and store it in the headerElement variable
  const headerElement = $('header');
  
  // Check if at least one headerElement exists
  if (headerElement.length !== 0) {
    // If the header element exists, change its text color to red (#FF0000)
    headerElement.css('color', '#FF0000');
  };
