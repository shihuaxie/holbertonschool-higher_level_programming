// Select the element with id = "toggle_header"
const toggleHeader = document.querySelector('#toggle_header');

// Add a click event listener to the element
toggleHeader.addEventListener('click', toggleHeaderColor);

// Define the function when the user clicks
function toggleHeaderColor() {
  // Select the <header> element
  const header = document.querySelector('header');

  // Check the current class and toggle between "red" and "green"
  if (header.classList.contains('red')) {
    // If header currently has class "red", remove it and add "green"
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // Otherwise (if it's green), remove it and add "red"
    header.classList.remove('green');
    header.classList.add('red');
  }
}
