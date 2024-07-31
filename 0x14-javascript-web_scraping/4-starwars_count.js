#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
const wedgeId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let num = 0;
    data.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        num++;
      }
    });
    console.log(num);
  }
});
