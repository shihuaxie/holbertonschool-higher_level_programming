// 1: Define the API URL
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// 2: Select the <ul> element where the movie titles will be added
const movieList = document.querySelector('#list_movies');

// 3: Fetch data from the API
fetch(url)
  // 4: Convert the response to JSON
  .then((response) => response.json())

  // 5: Use the data to display each movie title
  .then((data) => {
    // The API returns an object with a "results" array
    const movies = data.results;

    // Loop through all movies and add each one as an <li>
    movies.forEach((movie) => {
      // Create a new <li> element
      const listItem = document.createElement('li');

      // Set its text to the movie title
      listItem.textContent = movie.title;

      // Add it to the <ul> element
      movieList.appendChild(listItem);
    });
  })

  // 6: Handle any errors
  .catch((error) => console.log('Error fetching movies:', error));
