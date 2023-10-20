#!/usr/bin/node
const args = process.argv;
const c1 = args[2] ? args[2] : 'NaN';
const c3 = args[3] ? args[3] : 'NaN';
const c2 = parseInt(c1, 10);
const c4 = parseInt(c3, 10);
if (!c2) {
  console.log(0);
} else if (!c4) {
  console.log(0);
} else {
  const newarr = [];
  for (let i = 2; i < args.length; i++) {
    newarr.push(parseInt(args[i], 10));
  }
  newarr.sort((a, b) => a - b);
  console.log(newarr[newarr.length - 2]);
}
