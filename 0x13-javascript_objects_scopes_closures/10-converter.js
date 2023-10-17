#!/usr/bin/node
exports.converter = function (base) {
  return function realconv (number) {
    return (number.toString(base));
  };
};
