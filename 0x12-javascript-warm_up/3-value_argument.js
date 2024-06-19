#!/usr/bin/node

const [,, myArgs] = process.argv;
if (myArgs === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
