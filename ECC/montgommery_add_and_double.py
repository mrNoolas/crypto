

print('Montgomery curve addition and doubling\n\n')

print('For a curve of form B * v^2 = u^3 + A * u^2 + u \n ')
A = int(input('A: '))
B = int(input('B: '))

p = int(input('The curve is defined over the field F_p with p = '))

uInput = ""
while not uInput.startswith('q'):
    uInput = input("\nPossible options: Add, Double and Quit. All inputs must be ints. ").lower()

    if uInput.startswith('a'):
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))

        denX = pow(x2 - x1, -2, p)
        numX = (B * ((y2 - y1) ** 2)) % p
        x3 = (numX * denX - A - x1 - x2) % p

        denY_1 = pow(x2 - x1, -1, p)
        numY_1 = ((2 * x1 + x2 + A) * (y2 - y1)) % p
        denY_2 = pow(x2 - x1, -3, p)
        numY_2 = (B * ((y2 - y1) ** 3)) % p
        y3 = (numY_1 * denY_1 - numY_2 * denY_2 - y1) % p

        print('(x3, y3) = (' + str(x3) + ', ' + str(y3) + ')')

    elif uInput.startswith('d'):
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))

        denX = pow(2 * B * y1, -2, p)
        numX = (B * ((3 * (x1**2) + 2 * A * x1 + 1)**2)) % p
        x3 = (numX * denX - A - x1 - x1) % p

        denY_1 = pow(2 * B * y1, -1, p)
        numY_1 = ((2 * x1 + x1 + A) * (3 * (x1**2) + 2 * A * x1 + 1)) % p
        denY_2 = pow(2 * B * y1, -3, p)
        numY_2 = (B * ((3 * (x1**2) + 2 * A * x1 + 1) ** 3)) % p
        y3 = (numY_1 * denY_1 - numY_2 * denY_2 - y1) % p

        print('(x3, y3) = (' + str(x3) + ', ' + str(y3) + ')')