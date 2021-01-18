import math


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


print("Factoring RSA using Dixon's method\n\n")

n = int(input('Enter number to factor: '))
f = int(input('Maximum for primes (p < #) to use for factor-base: '))
F = rwh_primes(f)
print('Factor base: ', F)

uInput = input('\nEnter Quit or a number a: ').lower()
while not uInput.startswith('p'):
    a = int(uInput)
    b = pow(a, 2, n)

    rem = b
    factors = []
    for f in F:
        factorCoef = 0
        while rem % f == 0:
            rem //= f
            factorCoef += 1
        if factorCoef > 0:
            factors.append((f, factorCoef))

    if rem == 1:
        print('b: ', b, ' is smooth over F - ', factors)

        isSquare = True
        for factor in factors:
            if factor[1] % 2 != 0:
                isSquare = False
        print('b a square? ', isSquare)
        if isSquare:
            c = 1
            for f in factors:
                c = c * (f[0] ** (f[1] // 2))
            print('Factor of n: ', math.gcd(a - c, n))
    else:
        print('b: ', b, ' is not smooth over F')

    uInput = input('Enter Quit or a number a: ').lower()


