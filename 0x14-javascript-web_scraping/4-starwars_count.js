#!/usr/bin/node

/* display the status code of a GET request */
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieInfo = JSON.parse(body);
    let aux = 0;
    for (const i of movieInfo.results) {
      for (const j of i.characters) {
        if (j.search('18/') > 0) {
          aux++;
        }
      }
    }
    console.log(aux);
  }
});
