#!/usr/bin/node

// Define a function to calculate the factorial of a number
function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

// Call the factorial function with the number passed as the
// first command-line argument, parse it to a number using
// Number(), and print the result
console.log(factorial(Number(process.argv[2])));