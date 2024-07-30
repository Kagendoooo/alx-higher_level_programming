#!/usr/bin/node

const fs = require('fs');

// get file path from first argument
const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
