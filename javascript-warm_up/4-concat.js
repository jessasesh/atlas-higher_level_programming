#!/usr/bin/node
// Check if two arguments are passed to the script
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  // Print the two arguments in the specified format
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
