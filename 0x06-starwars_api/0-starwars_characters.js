#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}


/*const request = require('request');
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
*/
