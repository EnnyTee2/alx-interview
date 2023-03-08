#!/usr/bin/node

const request = require('request');
const process = require('process');

let url = 'https://swapi-api.alx-tools.com/api/films/';

let arg = process.argv[2]

const path = url + arg + '/'

request(path, (error, response, body) => {
  // Printing the error if occurred
    if(error) console.log(error)
   
    // Printing status code
    console.log(response.statusCode);
     
    // Printing body
    for (const idx of body) {
      if (idx == 'characters') {
        idx.forEach(character => {
          request(character, (error, response, body) => {
            console.log(body)
          });
        }
      }
    }
});
