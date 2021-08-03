#!/usr/bin/node
/* class: Rectangle that defines a Rectangle takes two arguments,
create a instance method for print() the Rectangle with an 'X',
rotate() for exchange the values of height and width,
double () for multiply the values of height and width. */
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
