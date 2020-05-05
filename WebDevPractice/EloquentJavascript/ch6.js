/*
My work through chapter 6 of Eloquent Javascript. This file 
has my solutions to the exercises, with additional challenges 
for extra practice.
Each exercise has examples in its corresponding multi-line comment
that can be uncommented to test the code
*/

/*
Write a class Vec that models vectors with the following:
- a constructor that takes an x and y value (Extra: make default x and y values 0)
- a plus method that adds another vector to the vector
-a minus method that subtracts another vector from the vector
-a length method that computes the distance from point (0,0)

Test Cases:

  console.log(new Vec(1, 2).plus(new Vec(2, 3)));
  // → Vec{x: 3, y: 5}
  console.log(new Vec(1, 2).minus(new Vec(2, 3)));
  // → Vec{x: -1, y: -1}
  console.log(new Vec(1, 2).minus(new Vec(2, 3)).plus(new Vec(10,5)));
  //→ Vec{x: 9, y: 4}
  console.log(new Vec(3, 4).length);
  // → 5  
  console.log(new Vec());
  //→ Vec{x: 0, y: 0}
*/

class Vec{
    constructor(x = 0, y = 0){
      this.x = x;
      this.y = y;
    }
    plus(other_vec){
      this.x += other_vec.x;
      this.y += other_vec.y;
      return this;
    }
    minus(other_vec){
        this.x -= other_vec.x;
        this.y -= other_vec.y;
      return this;
    }
    get length(){
      return (Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2)));
    }
  }

/*
Write a class Group that mimics a Javascript set with the following:
Constructor that generates a set from 0 or more values
A delete method that deletes a value from the set, if it exists in the set
An add method that adds a value to the set, if that value is not in the set
A has method that returns true if a value is in the set and false otherwise
A from method that constructs a set from an iterable, such as an array or map 
  
Test code:
let group = Group.from([10, 20]);
console.log(group.has(10));
// → true
console.log(group.has(30));
// → false
group.add(10);
group.delete(10);
console.log(group.has(10));
// → false

let objectSet = Group.from(new Map().set("a", "15").set("b", "20").set("b", "20"));
console.log(objectSet);
// → {set: [["a", "15"], ["b", "20"]]}
*/
class Group {
    constructor(...values){
      this.set = [];
      for (let value of values){
        this.add(value);
      }
    }
    
    add(value){
      if (!this.set.includes(value)) this.set.push(value);
    }
    delete(value){
      for (let index in this.set){
        if (this.set[index] === value) this.set.splice(index,1);
      }
    }
    
    has(value){
      for (let element of this.set){
        if (element === value) return true;
      }
      return false;
    }
    
    static from(iterableContainer){
      return new Group(...iterableContainer);
    }

    [Symbol.iterator](){ //To iterate through group
        return new GroupIterator(this);
    }
  }

/*
Write a GroupIterator class to make Group iterable

Example:
for (let value of Group.from(["a", "b", "c"])) {
  console.log(value);
}
// → a
// → b
// → c
*/
  class GroupIterator{
      constructor(group){
          this.group = group;
          this.position = 0;
      }
      next(){
          if (this.position >= this.group.set.length) return {done: true};
          const result = {value: this.group.set[this.position], done: false};
          this.position++;
          return result;
      }
  }
