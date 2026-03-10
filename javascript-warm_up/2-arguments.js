#!/usr/bin/node

const argsCount = process.argv.length - 2; // process.argv[0] = node, [1] = script name

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
