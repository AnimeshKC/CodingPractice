
/*
Write a class PGroup that functions similar to the Group class
of chapter 6 except instead of modifying a group, it constructs a 
new group. The constructor will not be part of the explicit interface
and instead PGroup.empty will be used to create an empty set. 

Tests:
let a = PGroup.empty.add("a");
let ab = a.add("b");
let b = ab.delete("a");

console.log(b.has("b"));
// → true
console.log(a.has("b"));
// → false
console.log(b.has("a"));
// → false
*/
class PGroup{
    constructor(set){
        this.set = set;
    }
    add(element){
        if (!this.has(element)){
            return new PGroup([...this.set, element]);
        }else{
            return this;
        }
    }
    delete(element){
        if (!this.has(element)) return this;
        return new PGroup(this.set.filter(m => m != element));
    }
    has(element){
        return this.set.includes(element);
    }
}
PGroup.empty = new PGroup([]);