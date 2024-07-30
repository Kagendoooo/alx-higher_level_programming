#!/usr/bin/node
// Star wars movie title
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

const movieId = process.argv[2];

request(`${url}/${movieId}/`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
