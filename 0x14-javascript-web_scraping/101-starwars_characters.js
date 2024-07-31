#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    const printCharacters = (index) => {
      if (index >= characters.length) {
        return;
      }
      request(characters[index], (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
          printCharacters(index + 1);
        }
      });
    };
    printCharacters(0);
  }
});
