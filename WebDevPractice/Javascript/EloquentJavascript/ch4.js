/*
write a range function that returns a list of numbers 
from a start value to an end value, inclusive, incrementing with 
a step value that defaults to 1

console.log(range(1, 10));
→ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(range(5, 2, -1));
→ [5, 4, 3, 2]
*/
function range(start, end, step = 1){
    let rangeArray = [];
    let currentNum = start;
    if (currentNum < end && step > 0){//if currentNum is less than end, step must be positive
        while (currentNum <= end){//requirement for inclusive
            rangeArray.push(currentNum);
            currentNum += step;
        }
    }
    else if (currentNum > end && step < 0){//if current num is greater than end, step must be negative
        while (currentNum >= end){ //requirement for descending to be inclusive
            rangeArray.push(currentNum);
            currentNum += step;
        }
    }
    else if (currentNum == end){ //if equal, the step is irrelevant
        rangeArray.push(currentNum);
    }
    return rangeArray;
}

/*
write a function sum that returns the sum of numbers in an array

console.log(sum(range(1, 10)));
→ 55

*/
function sum(numArray){
    let sumValue = 0;
    for (let num of numArray){
        sumValue += num;
    }
    return sumValue;
}


/*
Write a function reverseArray that, given an array, returns a new array with the position of all elements reversed
console.log(reverseArray(["A", "B", "C"]));
// → ["C", "B", "A"];
*/
function reverseArray(originalArray){
    let newArray = [];
    for (let index = originalArray.length - 1; index >= 0; index--){
        newArray.push(originalArray[index]);
    }
    return newArray;
}


/*
Write a function, reverseArrayInPlace, that reserves the position of elements 
of an array in place, i.e. without creating a new array.
This means that this is a function that creates a side effect.

let valueArray = [1, 2, 3, 4, 5];
reverseArrayInPlace(valueArray);
console.log(valueArray);
// → [5, 4, 3, 2, 1]
*/

function reverseArrayInPlace(valueArray){
    const stopValue = Math.floor(valueArray.length / 2);    
    for (let index = 0; index < stopValue; index++){
        const complementIndex = valueArray.length - index - 1;
        const complementTemp = valueArray[complementIndex];
        valueArray[complementIndex] = valueArray[index];
        valueArray[index] = complementTemp;
    }
}

/*
Write a function arrayToList that converts an array into a singly linked list

console.log(arrayToList([10, 20])); → {value: 10, rest: {value: 20, rest: null}}
*/

function arrayToList(array){ 
    let list = null;
    //iterate backwards to update list with the later lists
    for (let index = array.length - 1; index >=0; index--){ 
        list = {value: array[index], rest: list};
    }
    return list;
}
/*
Write a function listToArray that converts a list to an array

console.log(listToArray(arrayToList([10, 20, 30]))); -> [10, 20, 30]
*/
function listToArray(list){
    let array = [];
    while (list && list.value != null){
        array.push(list.value);
        list = list.rest;
    }
    return array;
}
/*
Write a function prepend that places an element at the front of a list

console.log(prepend(10, prepend(20, null)));
→ {value: 10, rest: {value: 20, rest: null}}
*/
function prepend(element, list){
    return {value: element, rest: list};
}

/*
Write a function nthElementInList that recursively finds the nth element of a list 
of the structure {value: v, rest: r} 

console.log(nthElementInList(arrayToList([10, 20, 30]), 1));
→ 20
*/
function nthElementInList(list, n){
    if (n == 0) return list.value;
    else if (n > 0) return nthElementInList(list.rest, n-1);
}

/*
Write a function deepEqual that checks whether the values of two entities a and b are equal

let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
→ true
console.log(deepEqual(obj, {here: 1, object: 2}));
→ false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
→ true
*/
function deepEqual(a, b){
    if (a === b) return true;
    if (a === null || b === null) return false;
    if (typeof a != "object" || typeof b != "object") return false;
    let keysA = Object.keys(a);
    let keysB = Object.keys(b);
    if (keysA.length != keysB.length) return false;
    for (let key of keysA){
        if (!keysB.includes(key) || !deepEqual(a[key], b[key])) return false;
    }
    return true;
}

let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
// → true
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// → true