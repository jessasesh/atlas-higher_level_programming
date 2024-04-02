#!/usr/bin/node

// Get the first argument from command line
const firstArg = process.argv[2];

// Get all arguments except the first one using slice
const arguments = process.argv.slice(2);

// Check if no arguments are provided
if (!firstArg) {
  console.log(0);
} 
// Check if only one argument is provided and it is '1'
else if (arguments.length === 1 && firstArg === '1') {
  console.log(0);
} 
// Otherwise, calculate the second-to-last argument
else {
  // Sort the arguments in ascending order
  arguments.sort((a, b) => a - b);
  
  // Get the index of the second-to-last argument
  let secondBigarg = arguments.length - 2;

  // Print the second-to-last argument
  console.log(arguments[secondBigarg]);
}