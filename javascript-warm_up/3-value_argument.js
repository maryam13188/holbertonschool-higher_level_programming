#!/usr/bin/node

const args = process.argv[2]; // أول وسيط بعد اسم الملف

if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
