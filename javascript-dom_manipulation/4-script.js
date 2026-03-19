#!/usr/bin/node

const addItem = document.getElementById('add_item');
let ul = document.querySelector('.my_list');

addItem.addEventListener('click', function() {
  const newListItem = document.createElement('li');
  newListItem.textContent = 'Item';
  ul.appendChild(newListItem);
});