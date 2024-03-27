#!/usr/bin/node
// Parse the first argument to an integer
const input = Number(process.argv[2]);

// Check if the parsed integer is not a number or if it's not provided
if (isNaN(input)) {
  // Handle if it's not a number or not provided
  console.log("Missing number of occurrences");
} else {
  // Handle for valid input
  for (let i = 0; i < input; input++) {
    console.log("C is fun");
  }
}
