#!/usr/bin/node
// Parse the first argument to an integer
const num = parseInt(process.argv[2]);

// Check if the parsed integer is not a number
if (!isNaN(num)) {
  // Handles if it's a valid number
  console.log('My number:', num);
} else {
  // Handles if the argument can't be converted to an integer
  console.log('Not a number');
}
