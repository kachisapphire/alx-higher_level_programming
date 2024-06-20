#!/usr/bin/node
function factorial (num) {
  if (num === 1 || num === 0 || isNaN(num)) {
    return (1);
  } return num * factorial(num - 1);
}
const arg = process.argv[2];
const n = parseInt(arg);
console.log(factorial(n));
