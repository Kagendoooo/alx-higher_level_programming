#!/usr/bin/node

const [,, myArg] = process.argv;
const num = parseInt(myArg, 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
