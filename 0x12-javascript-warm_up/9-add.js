#!/usr/bin/node
const argOne = process.argv[2];
const argTwo = process.argv[3];

function add (a, b) {
  a = parseInt(argOne);
  b = parseInt(argTwo);

  return a + b;
}

console.log(add(argOne, argTwo));
