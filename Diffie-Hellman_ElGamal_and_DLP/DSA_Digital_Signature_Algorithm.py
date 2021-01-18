
import random


def computeGenerators(p, l):
    generators = []
    for i in range(2, p):
        if (i**l) % p == 1 and (i**(l-1)) % p != 1:
            generators.append(i)
    return generators


print("DSA - Digital Signature Algorithm\n\n")

p = int(input('Number that defines the multiplicative group F_p p: '))

print('Choose g in F_p such that ord(g) = l, l is prime (thus l divides (p - 1))')
l = int(input('Ord(g) = l: '))
g = input('Calculate possible generators, Automatically choose generator or enter generator of cyclic group, g (c / a / [int g]): ')
if g.lower().startswith('c'):
    print(computeGenerators(p, l))
    g = int(input('g: '))
elif g.lower().startswith('a'):
    gs = computeGenerators(p, l)
    g = random.choice(gs)
    print('Chose g: ', g, ' from list ', gs)
else:
    g = int(g)


if (p - 1) % l != 0:
    print('l should be a devisor of the group order!!')
    exit(1)

# keygen:
a = int(input('Private Key a: '))
ha = pow(g, a, p)
print('Public key ha: ', ha)

uInput = ""
while not uInput.startswith('p'):
    uInput = input("\nPossible options: Sign, Verify and Quit. All inputs must be ints. ").lower()

    if uInput.startswith('s'):
        m = int(input('Message to sign (must be hashed): '))

        # Random Nonce k
        k = input('Random Nonce k, or Generate one ([k] / G): ')
        if k.lower().startswith('g'):
            k = random.randint(2, l)
            print('k: ', k)
        else:
            k = int(k)
        r = pow(g, k, p)
        print('r: ', r)

        r_bar = r % l
        k_inv = pow(k, -1, l)
        s = k_inv * (m + a * r_bar) % l
        print('Signature (r_bar, s) = (' + str(r_bar) + ', ' + str(s) + ')')

    elif uInput.startswith('v'):
        m = int(input('Hashed message to verify (must be hashed): '))
        r_bar = int(input('r_bar: '))
        s = int(input('s: '))

        w = pow(s, -1, l)
        u_1 = (m * w) % l
        u_2 = (r_bar * w) % l
        print('u_1 = m * w mod l = ', u_1, ' u_2 = r_bar mod l = ', u_2)

        v = (pow(g, u_1, p) * pow(ha, u_2, p)) % p
        v_bar = v % l
        print('v = g^(u_1) * ha^(u_2) mod p = ', v)
        print('v_bar = v mod l = ', v_bar)
        print('If valid, v_bar == r_bar. --> ', v_bar == r_bar)
