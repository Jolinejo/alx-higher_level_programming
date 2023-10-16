#!/usr/bin/node

const args = process.argv;
let fl = false;
for (let i = 2; args[i]; i++) {
    console.log(args[i]);
    fl = true;
}
if (!fl) {
  console.log('No argument');
}
