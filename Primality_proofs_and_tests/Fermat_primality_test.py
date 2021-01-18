
import random
import math

print("Fermat's primality test\n\n")

print('Caution, this test does not work for Carmichael numbers! They satisfy the test but are not prime.')
n = int(input('Enter number to test: '))

uInput = ""
while not uInput.startswith('p'):
    uInput = input("\n Possible options: Test again and Quit: ").lower()

    if uInput.startswith('t'):
        a = random.randint(2, n - 1)
        print('Selected random a = ', a)

        gcd = math.gcd(a, n)
        if gcd == 1:
            print('Step 1: gcd(a, n) = ', gcd, ' == 1 so go to step 2')

            power = pow(a, n - 1, n)
            if power == 1:
                print('Step 2: a^n-1 mod n = ', power, ' == 1 so MAYBE PRIME!')
            else:
                print('Step 2: a^n-1 mod n = ', power, ' != 1 so NOT PRIME!')
        else:
            print('Step 1: gcd(a, n) = ', gcd, ' != 1 so NOT PRIME!')





