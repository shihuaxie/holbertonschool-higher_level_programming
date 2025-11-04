#!/usr/bin/node

// Every row has 'size' * X
// Print X rows in total
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
