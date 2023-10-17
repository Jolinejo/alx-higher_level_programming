#!/usr/bin/node
function factorial (a) {
  const inte = parseInt(a, 10);
  if (!inte || inte === 1) { return (1); }
  return (a * factorial(a - 1));
}
const args = process.argv;
const c1 = args[2] ? args[2] : 'NaN';
console.log(factorial(c1));
