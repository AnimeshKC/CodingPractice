//Ch3 of Eloquent Javascript: functions
//My notes, exercise solutions, as well as some additional practice code

/*The book provides a function findSolution, that finds a solution to reach a target number,
with combinations of adding by 3 and multiplying by 5, starting from 1.
Examples: findSolution(24) -> (((1 * 3) + 5) * 3)
findSolution(15) -> null 

Personal Challenge: modify findSolution so that it can be provided the start num, the add and multiply numbers,
and program it such that it will find the shortest possible solution. 

Methodology: Use Breadth first search with an array of objects, where each object stores a current value
and a solution set
*/

function findSolution(target, startNum = 1, addNum = 5, mulNum = 3){
	let frontier = [{current: startNum, solution: `${startNum}`}];

	while (frontier.length){
		const front = frontier.shift();
		if (front.current == target) return front.solution;
		if ((front.current + addNum) <= target){
            const solutionString = `(${front.solution} + ${addNum})`;
			frontier.push({current: front.current + addNum, solution: solutionString});
		}
		if ((front.current * mulNum) <= target){
			const solutionString = `(${front.solution} * ${mulNum})`;
			frontier.push({current: front.current * mulNum, solution: solutionString});
		}
	}
}
console.log(findSolution(36,1, 9, 6));

//console.log(findSolution(24)); -> (((1 * 3) + 5) * 3)
//console.log(findSolution(36, 1, 9, 6)); -> ((1 * 6) * 6)
//console.log(findSolution(15)); -> undefined

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