#!/usr/bin/node
const [,, myArg] = process.argv;
const num = parseInt(myArg, 10);
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
