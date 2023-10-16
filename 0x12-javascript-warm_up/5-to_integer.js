#!/usr/bin/node

const args = process.argv;
const c1 = args[2] ? args[2] : 'Not a number';
const c2 = parseInt(c1, 10);
if (c2) {
  console.log('My number: ' + c2);
} else {
  console.log(c2);
}
