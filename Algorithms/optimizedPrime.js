/*
Optimized algorithm for checking when a number is prime 
O(sqrt(n)) runtime with constant time optimizations
*/

function isPrime(n) {
  //n must be a natural number for the result to make sense
  if (n <= 1) return false;
  if (n <= 3) return true;

  if (n % 2 == 0 || n % 3 == 0) return false;
  //if a number is prime, its square root is also prime
  //all prime numbers other than 2 and 3 follow a pattern of 6k +-1, where k is some integer
  for (let i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }
  return true;
}

/*
Algorithm for outputting all prime factors
*/

function primeFactors(n) {
  let factors = [];
  while (n % 2 == 0) {
    factors.push(2);
    n = n / 2;
  }
  //prime factors must be odd from this point onwards
  for (let i = 3; i * i <= n; i += 2) {
    while (n % i == 0) {
      factors.push(i);
      n = n / i;
    }
  }
  //if remaining number if greater than 2, it is a prime
  if (n > 2) factors.push(n);
  return factors;
}
// console.log(primeFactors(10)) => [2, 5]
