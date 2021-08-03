#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (const el in list) {
    rev.unshift(list[el]);
  }
  return rev;
};
