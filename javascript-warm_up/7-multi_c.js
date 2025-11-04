#!/usr/bin/node
const firstArg = process.argv[2];
const str = 'C is fun';

if (isNaN(firstArg) || firstArg < 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log(`${str}`);
  }
}
