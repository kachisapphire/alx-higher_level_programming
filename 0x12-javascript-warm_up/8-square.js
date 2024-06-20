#!/usr/bin/node
const args = process.argv[2];
const num = parseInt(args);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let i, square, j;
  for (i = 0; i < num; i++) {
    square = '';
    for (j = 0; j < num; j++) {
      square += 'x';
    }
    console.log(square);
  }
}
