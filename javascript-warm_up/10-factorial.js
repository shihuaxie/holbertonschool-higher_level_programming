#!/usr/bin/node
// n! = n × (n - 1) × (n - 2) × ... × 1
// recursion: factorial(0) = 1
// factorial(n) = n * factorial(n - 1)

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
