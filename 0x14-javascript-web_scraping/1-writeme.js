#!/usr/bin/node
// Script that writes a string to a file.

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
