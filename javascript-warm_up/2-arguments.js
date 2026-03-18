#!/usr/bin/node

// process.argv already automatically has 2 arguments. 
const count = process.argv.length - 2;

if (count === 0) {
    console.log('No argument');
} else if (count === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
