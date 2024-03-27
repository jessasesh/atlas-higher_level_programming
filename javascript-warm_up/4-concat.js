!#/usr/bin/node
// Check if two arguments are passed to the script
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  // Print the two arguments in the specified format
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  // Print an error message if two arguments are not provided
  console.log('Error: Please provide exactly two arguments.');
}
