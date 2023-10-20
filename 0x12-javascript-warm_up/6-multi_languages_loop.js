#!/usr/bin/node

const args = process.argv;
const langs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const toprint = args[2] ? langs.concat(args.slice(2, args.length)) : langs;
for (const i in toprint) {
  console.log(toprint[i]);
}
