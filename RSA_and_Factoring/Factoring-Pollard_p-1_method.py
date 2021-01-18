
import math

print("Factoring RSA using Pollard p-1 algorithm\n\n")

n = int(input('Enter number to factor: '))

# https://www.wolframalpha.com/input/?i=lcm%7B1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%7D
print('To get s as the lcm of a list, use wolfram alpha!')
s = int(input('s: '))

c = 1
first = True
while c == 1:
    if c == 1 and not first:
        print('c == 1, try again')
        first = False

    a = int(input('a: '))

    b = pow(a, s, n)
    print('b = a^s mod n = ', b)

    c = math.gcd(b-1, n)
    print('c = gcd(b - 1, n) =', c)
