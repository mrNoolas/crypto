
import math

print("Factoring RSA using Pollard-Rho (with Floyd's cycle finding algorithm)\n\n")

n = int(input('Enter number to factor: '))
c = int(input('Starting point c = '))
a = int(input('Offset a = '))

printSteps = input('Do you want to print the walks? (y/n): ').lower().startswith('y')
fastMode = input('Do you want to use fast mode? (combine gcd\'s) (y/n): ').lower().startswith('y')

slow = c
fast = c
p = math.gcd(fast - slow, n)

if fastMode:
    print("warning: buggy with large numbers?")
    while p == 1 or p == n:
        gcdProduct = 1
        for i in range(0, 10):
            slow = (slow**2 + a) % n
            fast = ((fast**2 + a)**2 + a) % n
            gcdProduct = (gcdProduct * (fast - slow)) % n

            if printSteps:
                print('Slow walk: ', slow, ' Fast walk: ', fast, ' GCD product:', gcdProduct)
        p = math.gcd(gcdProduct, n)
else:
    while p == 1 or p == n:
        slow = (slow**2 + a) % n
        fast = ((fast**2 + a)**2 + a) % n
        p = math.gcd(fast - slow, n)

        if printSteps:
            print('Slow walk: ', slow, ' Fast walk: ', fast)


print('Factor: ', p)
