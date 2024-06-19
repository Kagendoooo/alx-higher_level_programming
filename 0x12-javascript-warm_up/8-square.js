#!/usr/bin/node

const [,, sqr] = process.argv;
const num = parseInt(sqr, 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let r = '';
    for (let j = 0; j < num; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
