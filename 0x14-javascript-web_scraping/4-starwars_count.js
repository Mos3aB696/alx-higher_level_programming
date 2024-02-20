#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const char of film.characters) if (char.includes('18')) count++;
    }
    console.log(count);
  }
});
