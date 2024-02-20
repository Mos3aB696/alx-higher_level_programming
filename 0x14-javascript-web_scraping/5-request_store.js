#!/usr/bin/node

const request = require("request"),
  fs = require("fs");
const url = process.argv[2],
  path = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else
    fs.writeFile(path, body, "utf-8", (err) => {
      if (err) console.log(err);
    });
});
