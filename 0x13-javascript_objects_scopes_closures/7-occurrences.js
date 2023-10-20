#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      occ += 1;
    }
  }
  return (occ);
};
