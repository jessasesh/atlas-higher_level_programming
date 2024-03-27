#!/usr/bin/node
// Parse the first argument to an integer
const size = Number(process.argv[2]);
// Check if the parsed integer is not a number or if it's not provided
if (isNaN(size)) {
  // If it's not a number or not provided, print "Missing size"
  console.log("Missing size");
} else {
  // If it's a valid number, use a loop to print a square of X characters
  for (let i = 0; i < size; i++) {
    // Create a string of X characters of length equal to the size
    const row = 'X'.repeat(size);
    // Print the row
    console.log(row);
  }
}
