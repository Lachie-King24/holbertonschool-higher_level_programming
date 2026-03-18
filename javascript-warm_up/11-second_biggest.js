#!/usr/bin/node

const numbers = process.argv.slice(2);

if (numbers.length <= 1) {
  console.log(0);
} else {
  const number = numbers.map(Number).sort((a, b) => b - a);
  console.log(number[1]);
}
