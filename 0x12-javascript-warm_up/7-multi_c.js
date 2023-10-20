#!/usr/bin/node

const args = process.argv;
const c1 = args[2] ? args[2] : 'Not a number';
const c2 = parseInt(c1, 10);
if (!c2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < c2; i++) {
    console.log('C is fun');
  }
}
