#!/usr/bin/node
const args = process.argv[2];
const num = parseInt(args);
if (args === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  let i, square, j;
  for (i = 0; i < num; i++) {
    square = '';
    for (j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
