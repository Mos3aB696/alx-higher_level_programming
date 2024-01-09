#!/usr/bin/node
const arg = process.argv[2];
if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 1; j <= arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
