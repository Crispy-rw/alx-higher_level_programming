#!/usr/bin/node
// This function increments and calls a function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
