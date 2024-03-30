#!/usr/bin/node

function add (a, b) {
  // Parse the first command-line argument to an integer
  a = Number(process.argv[2]);
  // Parse the second command-line argument to an integer
  b = Number(process.argv[3]);

  // Check if both arguments are not valid numbers
  if (!a && !b) {
    return NaN; // Return NaN if both arguments are not valid numbers
  }
  
  // Return the addition of the two integers
  return a + b;
}

// Invoke the add function and store the result
const result = add();

// Print the result
console.log(result);
