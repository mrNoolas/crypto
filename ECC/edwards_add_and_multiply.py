
def addPoints(x1, y1, x2, y2):
    denx = pow((1 + d * x1 * x2 * y1 * y2), -1, p)
    deny = pow((1 - d * x1 * x2 * y1 * y2), -1, p)
    result_x = ((x1 * y2 + x2 * y1) * denx) % p
    result_y = ((y1 * y2 - a * x1 * x2) * deny) % p

    print('\nx = (x1 * y2 + x2 * y1) / (1 + d * x1 * x2 * y1 * y2) mod p ')
    print('  = (' + str(x1) + ' * ' + str(y2) + ' + ' + str(x2) + ' * ' + str(y1) + ') / ( 1 + ' +
          str(d) + ' * ' + str(x1) + ' * ' + str(x2) + ' * ' + str(y1) + ' * ' + str(y2) + ') mod p')
    print('   = ' + str(x1 * y2 + x2 * y1) + ' / ' + str(1 + d * x1 * x2 * y1 * y2) + ' mod p')
    print('   = ' + str(result_x))

    print('y = (y1 * y2 - a * x1 * x2) / (1 - d * x1 * x2 * y1 * y2) mod p')
    print('  = (' + str(y1) + ' * ' + str(y2) + ' - ' + str(x1) + ' * ' + str(x2) + ') / ( 1 - ' +
          str(d) + ' * ' + str(x1) + ' * ' + str(x2) + ' * ' + str(y1) + ' * ' + str(y2) + ') mod p')
    print('   = ' + str(y1 * y2 - a * x1 * x2) + ' / ' + str(1 - d * x1 * x2 * y1 * y2) + ' mod p')
    print('   = ' + str(result_y))

    return result_x, result_y


print('(Twisted) Edwards curve addition\n\n')

print('For a curve of form ax^2 + y^2 = 1 + dx^2 * y^2 \n ' +
      'where a is a square and d is not a square, or a = 1 and d is a square')
a = int(input('a: '))
d = int(input('d: '))

p = int(input('The curve is defined over the field F_p with p = '))

uInput = ""
while not uInput.startswith('q'):
    uInput = input("\nPossible options: Add, Multiply and Quit. All inputs must be ints. ").lower()

    if uInput.startswith('a'):
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))
        x, y = addPoints(x1, y1, x2, y2)

        print('(x, y) = (' + str(x) + ', ' + str(y) + ')')

    elif uInput.startswith('m'):
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        s = int(input('scalar: '))

        x, y = 0, 1  # neutral element
        print('')
        for i in range(1, s + 1):
            x, y = addPoints(x, y, x1, y1)
            print('\n(x, y) = s * (x1, y1) + (x2, y2) = ' + str(s - i) + ' * ('
                  + str(x1) + ', ' + str(y1) + ') + (' + str(x) + ', ' + str(y) + ')')

        print('\n\n(x, y) = ' + str(s) + ' * ('
              + str(x1) + ', ' + str(y1) + ') = (' + str(x) + ', ' + str(y) + ')')

