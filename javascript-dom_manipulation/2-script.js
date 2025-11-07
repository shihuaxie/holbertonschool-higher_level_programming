// select the id = red_header
const redHeader = document.querySelector('#red_header');

// add an event listner - click
redHeader.addEventListener('click', addRedClass);

function addRedClass() {
  // select <header>
  const header = document.querySelector('header');

  // add class = "red"
  header.classList.add('red');
}
