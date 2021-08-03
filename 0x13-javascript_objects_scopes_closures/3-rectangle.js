#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.height = Number(h);
      this.width = Number(w);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log(`${Array(this.width).fill('X').join('')}`);
    }
  }
}

module.exports = Rectangle;
