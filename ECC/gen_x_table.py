
print('Generate a table of x^2 and x^-1 mod p')

p = int(input('The curve is defined over the field F_p with p = '))

firstLine = 'x    || '
sqLine =    'x^2  || '
signLine =  '     || '
invLine =   'x^-1 || '

x_squared = ['0']
x_inv = [{'-': 'n/a', '+': 'n/a'}]

firstLine += '0   | '
sqLine +=    '0   | '
signLine +=  '- + | '
invLine +=   'n/a | '

for x in range(1, (p - 1) // 2 + 1):
    x_squared.append(str(pow(x, 2, p)))
    x_inv.append({'-': str(pow(-x, -1, p)), '+': str(pow(x, -1, p))})

    width = len(x_inv[x]['+']) + len(x_inv[x]['-']) + 2
    firstLine += str(x)
    firstLine += ' ' * (width - len(str(x)))
    firstLine += '| '

    sqLine += x_squared[x]
    sqLine += ' ' * (width - len(x_squared[x]))
    sqLine += '| '

    signLine += '-' + ' ' * (len(x_inv[x]['-']))
    signLine += '+' + ' ' * (len(x_inv[x]['+']))
    signLine += '| '

    invLine += x_inv[x]['-'] + ' ' + x_inv[x]['+'] + ' | '

print(firstLine)
print(sqLine)
print(signLine)
print(invLine)
