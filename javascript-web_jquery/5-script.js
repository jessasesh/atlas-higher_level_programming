$(document).ready(function () {
  const addListItem = $('#add_item');

  addListItem.click(function () {
    const myList = $('.my_list');
    const newListItem = $('<li>Item</li>');

    myList.append(newListItem);
  });
});
