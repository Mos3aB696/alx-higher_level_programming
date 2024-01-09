#!/usr/bin/node
const arg = process.argv;
arg.shift();
arg.shift();

if (arg[0]) {
  console.log(arg[0]);
} else {
  console.log('No argument');
}
