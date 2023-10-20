#!/usr/bin/node

const args = process.argv;
const c1 = args[2] ? args[2] : 'Not a number';
const c2 = parseInt(c1, 10);
if (!c2) {
  console.log('Missing size');
} else {
  for (let i = 0; i < c2; i++) {
    let str = '';
    for (let j = 0; j < c2; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
