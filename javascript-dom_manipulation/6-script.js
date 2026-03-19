#!/usr/bin/node

let character = document.getElementById('character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  // Take the data from fetch and return it in json format
  .then(response => {
    return response.json();
  })
  // using json from response, change text.content of character to the name from the url.
  .then(data => {
    character.textContent = data.name;
  })
  // Error handling just in case
  .catch(error => {
    console.error('Error fetching data:', error);
  });