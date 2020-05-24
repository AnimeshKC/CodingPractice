//Given three numbers x, y, and p, compute (xˆy) % p.

function modularExponentiation(base, exponent, modulus) {
  if (modulus == 1) return 0;
  let value = 1;
  //the below loop enables calculating modular exponentiation for larger values
  //than the naive approach.
  /*
    if a * b = c, then c mod m = (a * b) mod m = [[a mod m] [b mod m]] mod m
  */
  //(a * b) % M = [(a % M) * (b%M)] % M
  //so (base * base) exponent times mod M can be decomposed
  for (let i = 0; i < exponent; i++) {
    value = (value * base) % modulus;
  }
}
