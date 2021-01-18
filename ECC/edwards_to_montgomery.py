

# Montgomery curve, special kind of weierstrass curve: B * v^2 = u^3 + A * u^2 + u for A != +-2, B != 0
print('Edwards curve to Montgomery curve\n\n')

print('For an edwards curve of form ax^2 + y^2 = 1 + dx^2 * y^2 \n ' +
      'where a is a square and d is not a square, or a = 1 and d is a square')
a = int(input('a: '))
d = int(input('d: '))
p = int(input('The curve is defined over the field F_p with p = '))

den = pow(a - d, -1, p)
numA = (2 * (a + d)) % p
A = (numA * den) % p
B = (4 * den) % p

if abs(A) == 2 or B == 0:
    print('could not convert')
    exit(1)

print('A: ' + str(A) + '; B: ' + str(B))
print('Montgomery curve: ' + str(B) + ' * v^2 = u^3 + ' + str(A) + ' * u^2 + u')

uInput = ""
while not uInput.startswith('q'):
    uInput = input("\nPossible options: New point to convert or Quit. All other inputs must be ints. ").lower()

    if uInput.startswith('n'):
        x = int(input('x: '))
        y = int(input('y: '))

        denU = pow(1 - y, -1, p)
        denV = pow(x * (1 - y), -1, p)
        num = (1 + y) % p

        u = (num * denU) % p
        v = (num * denV) % p
        x_inv = pow(x, -1, p)
        check = v == (u * x_inv) % p
        print('Check: ', check)
        print('(x, y) --> (u, v) = (' + str(u) + ', ' + str(v) + ')')
