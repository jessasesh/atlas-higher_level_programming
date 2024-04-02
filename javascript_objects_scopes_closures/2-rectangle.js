#!/usr/bin/node

// Define class
class Rectangle {
  constructor (w, h) {
    // Check if width and height
    // are not negative or 0
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// Exports this class
module.exports = Rectangle;
