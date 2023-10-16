#!/usr/bin/node

const args = process.argv;
let fl = 0;
args.forEach((val, index) => {
  if (index > 1) {
    console.log(val);
    fl = 1;
  }
});
if (fl === 0) {
  console.log('No argument');
}
