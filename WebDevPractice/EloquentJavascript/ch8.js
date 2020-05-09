/*
Chapter 8 of Eloquent Javascript
My solutions to the exercise questions, alongside the 
usage of assert for tests
*/
const assert = require('assert')
class MultiplicatorUnitFailure extends Error {}

/*
Given the function primitiveMultiply below, write a function reliableMultiply
that takes the same input parameters and wraps the primitive function
and repeats until an error is not thrown
*/
function primitiveMultiply(a, b) {
  if (Math.random() < 0.2) {
    return a * b;
  } else {
    throw new MultiplicatorUnitFailure("Klunk");
  }
}

function reliableMultiply(a, b) {

  try{
    return primitiveMultiply(a, b);
  }catch(e){
    if (e instanceof MultiplicatorUnitFailure){
      return reliableMultiply(a, b); //recurse until no error
    }
    else{
        throw e;
    }
  }
}

//test
assert.equal(reliableMultiply(8, 8), 64);


/*
given a structure below, box, write a function withBoxUnlocked
that executes a function. If the box was locked, it will first unlock
the box and the lock it afterwards.
*/
const box = {
    locked: true,
    unlock() { this.locked = false; },
    lock() { this.locked = true;  },
    _content: [],
    get content() {
      if (this.locked) throw new Error("Locked!");
      return this._content;
    }
  };
  
  function withBoxUnlocked(body) {
    if (!box.locked) {
      return body();
    }
    box.unlock();
    try {
      return body();
    } finally {
      box.lock();
    }
  }

//test
let a;
withBoxUnlocked(() => {
    a = box.content; 
    a.push("gold pieces");
});
assert.deepEqual(a, ["gold pieces"]);