//Ch3 of Eloquent Javascript
//My notes, exercise solutions, as well as some additional practice code

/*Create a function that given a target number, 
returns a combination of adding by 3 or multiplying by 5
, starting from 1, such that the target number is found */

function findSolution(target){
	function find(current, history, state = "add"){
		if (current == target){
		return history;	
		}else if (current > target) return null;
		else{
		return find(current + 5, `(${history} + 5`) ||
		find(current * 3, `(${history} * 3`);
		}
	}
	return find(1, "1");
}
//findSolution(24) -> (((1 * 3) + 5) * 3)
//findSolution(15) -> null

//Use recursion to formulate an alternative means of checking whether a number is even
function isEven(N){
  if (N == 0) return true;
  else if (Math.abs(N) == 1) return false;
  return isEven(Math.abs(N)-2);
}

//isEven(50)→ true
//isEven(75) -> false
//isEven(-1) -> false
//isEven(-2) -> true

//create a function that returns the number of occurances of a character
function countChar(inputString, charToCount){
  let count = 0;
  for(let number = 0; number < inputString.length; number+= 1){
    if (inputString[number] == charToCount) count++;
  }
  return count;
}
//console.log(countChar("kakkerlak", "k"));  → 4