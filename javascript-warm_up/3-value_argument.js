#!/usr/bin/node
// Check if the first argument passed to the script is undefined
if (process.argv[2] === undefined) {
    // Print "No argument" if no argument is passed
    console.log("No argument");
} else {
    // Print the value of the first argument if it is defined
    console.log(process.argv[2]);
}
