#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const [,, int1, int2] = process.argv;
const num1 = parseInt(int1, 10);
const num2 = parseInt(int2, 10);
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  const sum = add(num1, num2);
  console.log(sum);
}
