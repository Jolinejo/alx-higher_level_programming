#!/usr/bin/node

const args = process.argv;
const c1 = args[2] ? args[2] : 'undefined';
const c2 = args[3] ? args[3] : 'undefined';
console.log(c1 + ' is ' + c2);
