#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  // Constructor function to initialize width and height
  constructor(w, h) {
    // Check if width or height is non-positive
    if (w <= 0 || h <= 0) {
      // Return an empty object if width or height is invalid
      return {};
    } else {
      // Initialize width and height properties
      this.width = w;
      this.height = h;
    }
  }

  // Instance method to print the rectangle
  print() {
    // Check if width or height is not defined
    if (!this.width || !this.height) {
      return;
    }
    // Print the rectangle using 'X' character
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method to rotate the rectangle
  rotate() {
    // Swap width and height
    [this.width, this.height] = [this.height, this.width];
  }

  // Instance method to double the dimensions of the rectangle
  double() {
    // Double width and height
    this.width *= 2;
    this.height *= 2;
  }
}

// Export the Rectangle class
module.exports = Rectangle;
