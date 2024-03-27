#!/usr/bin/node
// Check if two arguments are passed, concats, and prints
console.log(
	(process.argv[2] || 'undefined') + ' is ' + (process.argv[3] || 'undefined')
);
