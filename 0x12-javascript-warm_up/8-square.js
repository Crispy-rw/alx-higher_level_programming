#!/usr/bin/node

const occur = parseInt(process.argv[2]);

if (isNaN(occur) || occur == undefined){
  console.log('Missing size');
}else{
  let i = 0;
  while(i < occur){
    console.log(`${Array(occur).fill('X').join('')}`);
    i++;
  }
}
