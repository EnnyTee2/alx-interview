#!/usr/bin/node

const request = require('request');
const process = require('process');

let url = 'https://swapi-api.alx-tools.com/api/films/';

let arg = process.argv[2];

const path = url + arg + '/'

request(path, (error, response, body) => {
  const message = JSON.parse(body).characters;
      //console.log(message)
  for (const idx of message) {
    request(idx, (err, resp, body) => {
      let name = JSON.parse(body).name;
      console.log(name);
    });
  }
})
