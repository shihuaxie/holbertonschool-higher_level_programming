#!/usr/bin/node
const firstArg = process.argv[2];
const str = 'C is fun';

for (i = 0; i < firstArg; i++) {
  console.log(`${str}`);
}
