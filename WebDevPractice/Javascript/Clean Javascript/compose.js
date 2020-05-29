/*
compose takes a varible number of functions, creates an array "functions" with it, then
given an initial value, applies all the functions from right to left 

pipe does the same but from left to right
*/
const compose = (...functions) => (initial) =>
  functions.reduceRight((arg, fn) => fn(arg), initial);
const pipe = (...functions) => (initial) =>
  functions.reduce((arg, fn) => fn(arg), initial);

function add1(value) {
  return value + 1;
}

function mul2(value) {
  return value * 2;
}

let com1 = compose(add1, mul2)(2);
let pip1 = pipe(add1, mul2)(2);
console.log(com1);
console.log(pip1);
