#!/usr/bin/node

argv1 = parseInt(process.argv[2]);
argv2 = parseInt(process.argv[3]);

function add(a, b){
  return a + b;
}

console.log(add(argv1, argv2));
