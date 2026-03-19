const url = "https://swapi-api.hbtn.io/api/films/?format=json"
let movieList = document.getElementById('list_movies');

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    const movies = data.results;
    for (const movie of movies) {
      const newListItem = document.createElement('li')
      newListItem.textContent = movie.title;
      movieList.appendChild(newListItem);
    }
  })
  .catch(error => {
    console.error('Error fetching data:', error)
  })