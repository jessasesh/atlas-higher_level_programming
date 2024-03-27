#!/usr/bin/node
// Parse the first argument to an integer
const argv2 = process.argv[2];
// Handle bad input
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
// Allows iteration of print statement to be specified
for (let x = 0; x < argv2; x++) {
  console.log('C is fun');
}
