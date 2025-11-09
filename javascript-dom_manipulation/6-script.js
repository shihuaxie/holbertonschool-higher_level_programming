// 1: The API URL we want to get data from
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// 2: Get the <div> element where we’ll show the character’s name
const character = document.querySelector('#character');

// 3: Fetch data from the API
fetch(url)
  // 4: Convert the response to JSON (so JavaScript can read it)
  .then((response) => response.json())

  // 5: Get the character’s name from the data and display it
  .then((data) => {
    character.textContent = data.name;
  })

  // 6: If something goes wrong, show an error in the console
  .catch((error) => console.log('Error:', error));
