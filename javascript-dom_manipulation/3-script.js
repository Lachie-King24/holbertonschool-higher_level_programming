#!/usr/bin/node

const togHeader = document.getElementById('toggle_header');
const header = document.querySelector('header');

togHeader.addEventListener('click', function() {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});