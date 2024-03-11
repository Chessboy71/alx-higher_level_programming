#!/usr/bin/node

const { argv } = require('node:process');

let num = parseInt(argv[2]);

if (num !== NaN){
    console.log(`My number: ${num}`);
}
else {
    console.log('Not a number')
}