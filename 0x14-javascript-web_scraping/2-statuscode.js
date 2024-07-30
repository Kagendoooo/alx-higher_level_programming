#!/usr/bin/node
// Script that display the status code of a GET request.

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error == null) {
    console.log(`code: ${response.statusCode}`);
  }
});
