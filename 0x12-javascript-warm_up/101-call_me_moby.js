#!/usr/bin/node
// This function executes x times a function
exports.callMeMoby = function (x, thefunction) {
  for (let i = 0; i < x; i++) {
    thefunction();
  }
};
