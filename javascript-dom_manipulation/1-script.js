// select the element where id = red_header
const redHeader = document.querySelector('#red_header');

// add an eventlistener(click) to redheader
redHeader.addEventListener('click', changeHeaderColor);

// define the func when the click is triggered
function changeHeaderColor() {
  // select header ele
  const header = document.querySelector('header');
  // update color
  header.style.color = '#FF0000';
}
