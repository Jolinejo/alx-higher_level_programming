#!/usr/bin/node

const args = process.argv;
let fl = false;
for (let i = 2; i < 3; i++) {
  console.log(args[i]);
  fl = true;
}
if (!fl) {
  console.log('No argument');
}
