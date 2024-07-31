#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  const done = {};
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  json.forEach(element => {
    if (element.completed) {
      if (!done[element.userId]) {
        done[element.userId] = 0;
      }
      done[element.userId]++;
    }
  });
  console.log(done);
});
