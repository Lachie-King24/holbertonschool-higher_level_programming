document.addEventListener('DOMContentLoaded', function () {
const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
let hello = document.getElementById('hello');

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    hello.textContent = data.hello;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  })
});
