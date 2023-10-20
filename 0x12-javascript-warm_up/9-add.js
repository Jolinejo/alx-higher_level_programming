#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const args = process.argv;
const c1 = args[2] ? args[2] : 'NaN';
const c3 = args[3] ? args[3] : 'NaN';
const c2 = parseInt(c1, 10);
const c4 = parseInt(c3, 10);
if (!c2) {
  console.log('NaN');
} else if (!c4) {
  console.log('NaN');
} else {
  console.log(add(c2, c4));
}
