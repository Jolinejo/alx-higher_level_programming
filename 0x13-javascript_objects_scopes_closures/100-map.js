#!/usr/bin/node
const listOri = require('./100-data.js').list;

console.log(listOri);
console.log(listOri.map((x, index) => x * index));
