// 1: Select the element id =  "update_header"
const updateHeader = document.querySelector('#update_header');

// 2: Add a click event listener to that element
updateHeader.addEventListener('click', changeHeaderText);

// 3: Define the function that runs when the user clicks
function changeHeaderText() {
  // 4: Select the <header> element
  const header = document.querySelector('header');

  // 5: Change its text to "New Header!!!"
  header.textContent = 'New Header!!!';
}
