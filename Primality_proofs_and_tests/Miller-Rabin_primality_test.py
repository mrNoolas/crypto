
print("Miller-Rabin primality test\n\n")

n = int(input('Enter number to test: '))

b = int(input('\n Step 1: pick random b: '))


print('\n Step 2: compute c^t mod n')
print('First compute t: n-1 = 2^s * t')

s = 0
t = n - 1
while t % 2 == 0:
    s += 1
    t //= 2

c = pow(b, t, n)
print('t = ', t, '; c = ', c, '; s = ', s)


print('\n Step 3: if c = +-1 it may be a prime')
if c == 1 or c == n - 1:
    print('MAYBE PRIME!')
    exit(0)


print('\n Step 4: keep increasing t up to n-1 to check if c is congruent to 1 mod n')
for T in range(1, s):
    c = pow(c, 2, n)
    print('T:', T, ' c:', c)

    if c == 1:
        print('NOT PRIME')
        exit(0)
    elif c == n - 1:
        print('MAYBE PRIME')
        exit(0)

print('NOT PRIME')