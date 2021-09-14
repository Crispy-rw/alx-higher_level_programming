#!/usr/bin/node
/* display the status code of a GET request */
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieInfo = JSON.parse(body);
    console.log(movieInfo.title);
  }
});
