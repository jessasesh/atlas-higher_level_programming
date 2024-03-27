#!/usr/bin/node
// Check if no arguments are passed
if (process.argv.length === 2) {
  console.log('No argument');
} 
// Check if only one argument is passed
else if (process.argv.length === 3) {
  console.log('Argument found');
} 
// More than one argument is passed
else {
  console.log('Arguments found');
}
