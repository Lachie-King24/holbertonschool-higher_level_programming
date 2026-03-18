#!/usr/bin/node

const count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    let row = '';
    for (let j = 0; j < count; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
