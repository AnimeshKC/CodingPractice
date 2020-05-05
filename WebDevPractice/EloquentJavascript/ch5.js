/*
Chapter 5 of Eloquent Javascript
My exercise solutions, and potentially extra practice code
*/

/*
Create a function that flattens an array of arrays into a single array,
using reduce and concat

console.log(flatten([[1, 2, 3], [4, 5], [6]])); -> [1, 2, 3, 4, 5, 6]
*/

function flatten(nestedArray){
    return nestedArray.reduce((accumulator, currentArray) => 
    accumulator.concat(currentArray));
}

/*
Write a higher-order function, loop(value, testFunc, updateFunc, bodyFunc)
that executes bodyFunc(value) in a loop, 
updating value with the return value of updateFunc(value),
as long as testFunc(value) is true. 

In other words, this function mimics a for loop

loop(3, n => n > 0, n => n - 1, console.log); -> 
3
2
1
*/

function loop(value, testFunc, updateFunc, bodyFunc){
    while (testFunc(value)){
        bodyFunc(value);
        value = updateFunc(value);
    }
}

/*
Write a function every(array, testFunc),

that returns true if for each element in array, testFunc(element) is true.
Otherwise, returns false. 

console.log(every([1, 3, 5], n => n < 10));
// → true
console.log(every([2, 4, 16], n => n < 10));
// → false
console.log(every([], n => n < 10));
// → true
*/
function every(array, testFunc){
    for (let element of array){
        if (!testFunc(element)) return false;
    }
    return true;
}

/*
function dominantDirection(text) requires the data files 
from https://eloquentjavascript.net/code

It finds the most dominant writing style (i.e. ltr = left-to-right;
    rtl = right-to-left) among characters within a string

console.log(dominantDirection("Hello!"));
// → ltr
console.log(dominantDirection("Hey, مساء الخير"));
// → rtl
*/
function dominantDirection(text) {
    let counted = countBy(text, char => {
      let script = characterScript(char.codePointAt(0));
      return script ? script.direction : "none";
    }).filter(({name}) => name != "none");
  
    if (counted.length == 0) return "ltr";
  
    return counted.reduce((a, b) => a.count > b.count ? a : b).name;
  }
