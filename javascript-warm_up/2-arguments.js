#!/usr/bin/node
// Check if no arguments are passed
if (process.argv.length === 2) {
    console.log("No argument");
} 
// Checks for only one argument is passed
else if (process.argv.length === 3) {
    console.log("Argument found");
} 
// Handles more than one argument
else {
    console.log("Arguments found");
}
