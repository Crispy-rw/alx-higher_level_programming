#!/usr/node/bin

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
