#!/usr/bin/node

// Define a function named 'add' that takes two integer parameters
function add(a, b) {
  return a + b;
}

// Make the 'add' function visible from outside by exporting it
module.exports = add;