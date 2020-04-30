from itertools import count, islice

def is_prime(n: int)-> bool:
    if n < 2:
        return False
    factorToCheck = 2
    while factorToCheck*factorToCheck <=n:
        if n % factorToCheck == 0:
            return False
        factorToCheck += 1
    return True

def sum_n_Primes(n: int) ->int:
    '''Computes the sum of the first n primes'''
    return sum(islice((x for x in count() if is_prime(x)), n))
def main():
    assert(sum_n_Primes(1000) == 3682913)
    print("Tests have passed")

if __name__ == "__main__":
    main()
