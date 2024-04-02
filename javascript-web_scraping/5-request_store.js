#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (error, response, body) {
  fs.writeFile(filePath, body, 'utf8', function (error) {
    if (error) {
      console.error(error);
    }
  });
});