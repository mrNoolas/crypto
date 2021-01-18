
from sympy.ntheory.modular import crt

def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


print('Pohlig-Hellman method for solving DLP\n\n')

p = int(input('Number that defines the multiplicative group p: '))
g = int(input('Generator of the group g: '))
n = p - 1  # Group order
h = int(input('Challenge h for which to find log_g h = a; h: '))

# factor the group order n
primes = rwh_primes(n // 2 + 1)
factors = []  # or enter them as [(p_0, e_0), ..., (p_i, e_i)]
x = n
for prime in primes:
    factorCoef = 0
    while x % prime == 0:
        x //= prime
        factorCoef += 1
    if factorCoef > 0:
        factors.append((prime, factorCoef))

print('Factors of ', n, ': ', factors)


a = [[] for i in range(len(factors))]  # intermediate results for each subgroup
A = []

for i in range(len(factors)):
    p_i = factors[i][0]
    e_i = factors[i][1]

    logTable = []
    g_npi = pow(g, n // p_i, p)
    for x in range(p_i):
        logTable.append(pow(g_npi, x, p))
    print('\nLog Table for p_i = ', p_i, ' Logtable: ', logTable)

    # solve j = 0 seperately:
    hl = h
    exp = n // p_i
    eq_value = pow(hl, exp, p)
    for x in range(len(logTable)):
        if logTable[x] == eq_value:
            a[i].append(x)  # a[i][0]
    print('h\' = ', hl)
    print('a[' + str(i) + '][0] = ' + str(a[i][0]))

    if e_i > 1:
        g_inv = pow(g, -1, p)

        for j in range(1, e_i):
            hl = hl * pow(g_inv, a[i][j-1] * p_i ** (j-1), p) % p

            # calc log_g^(n/p_i) (hl)^(n/(p_i^(j+1))
            exp = n // (p_i ** (j + 1))
            eq_value = pow(hl, exp, p)
            for x in range(len(logTable)):
                if logTable[x] == eq_value:
                    a[i].append(x)  # a[i][j]
                    break

            print('h\' = ', hl)
            print('a[' + str(i) + '][' + str(j) + '] = ' + str(a[i][j]))

    sum = 0
    for j in range(0, e_i):
        sum += a[i][j] * (p_i ** j)

    A.append((sum, p_i, e_i))

print('\n\nApply CRT to the following autcomes:')
m = []
v = []
for (a, p_i, e_i) in A:
    m.append(p_i**e_i)
    v.append(a)
    print('a = ', a, ' mod ' + str(p_i) + '^' + str(e_i))

outcome = crt(m, v, False, False)[0]
print('CRT: ', outcome)
print('\nCheck g^a == h: ' + str(g) + '^' + str(outcome) + ' = ' + str(pow(g, outcome, p)) + ' == ' + str(h) + ' --> ', pow(g, outcome, p) == h)


