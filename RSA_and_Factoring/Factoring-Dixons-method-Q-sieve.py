import math


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def factorOverBase(x):
    factors = []
    for f in F:
        factorCoef = 0
        while x % f == 0:
            x //= f
            factorCoef += 1
        if factorCoef > 0:
            factors.append((f, factorCoef))

    if x == 1:
        return True, factors
    return False, factors


print("Factoring RSA using Dixon's method\n\n")

n = int(input('Enter number to factor: '))
f = int(input('Maximum for primes (p < #) to use for factor-base: '))
F = rwh_primes(f)
print('Factor base: ', F)

i = int(input('Amount of numbers to pick, i: '))

factoredPairs = []
for a in range(1, i + 1):
    b = n + a

    smooth, factorsA = factorOverBase(a)
    if smooth:
        smooth, factorsB = factorOverBase(b)
        if smooth:
            factoredPairs.append((a, factorsA, b, factorsB))

for (a, factorsA, b, factorsB) in factoredPairs:
    string = '{0:50}  {1}'.format(str(a) + ' ' + str(factorsA), str(b) + ' ' + str(factorsB))
    print(string)
