#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/';

request(filmUrl + movieId, async function (err, res, body) {
  if (err) return console.error(err);
  const charList = JSON.parse(body).characters;

  for (const charURL of charList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
