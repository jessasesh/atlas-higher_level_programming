$(document).ready(function () {
  const addHeader = $('#update_header');

  addHeader.click(function () {
    const myHeader = $('header');
    myHeader.text('New Header!!');
  });
});
