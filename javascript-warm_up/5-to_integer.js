#!/usr/bin/node
const fistArg = process.argv[2];
const num = parseInt(fistArg);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
