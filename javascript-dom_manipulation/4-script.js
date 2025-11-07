// Select the element with id "add_item"
const addItem = document.querySelector('#add_item');

// Add a click event listener to it
addItem.addEventListener('click', addNewItem);

// Define the function that runs when the user clicks
function addNewItem() {
  // Select the <ul> element with class "my_list"
  const list = document.querySelector('.my_list');

  // Create a new <li> element
  const newItem = document.createElement('li');

  // Set the text content of the new <li> element
  newItem.textContent = 'Item';

  // Append (add) the new <li> element to the list
  list.appendChild(newItem);
}
