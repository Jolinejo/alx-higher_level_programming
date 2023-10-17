#!/usr/bin/node
exports.esrever = function (list) {
  const occ = [];
  for (let i = list.length - 1; i !== -1; i--) {
    occ.push(list[i]);
  }
  return (occ);
};
