document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch((error) => {
      document.querySelector('#hello').textContent = 'Error loading translation';
      console.error('Error:', error);
    });
});
