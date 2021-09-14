#!/usr/bin/node
/* computes the number of tasks completed by user id. */
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const jsonFile = JSON.parse(body);
    const taskComplete = {};
    for (const i in jsonFile) {
      const data = jsonFile[i];
      if (data.completed === true) {
        const id = data.userId;
        if (id in taskComplete) {
          taskComplete[id]++;
        } else {
          taskComplete[id] = 1;
        }
      }
    }
    console.log(taskComplete);
  }
});
