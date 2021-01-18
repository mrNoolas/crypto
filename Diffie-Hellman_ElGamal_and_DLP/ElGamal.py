import random

print("ElGamal\n\n")

p = int(input('Group order prime p: '))
g = int(input('Generator for F_p g: '))

a = int(input('Private key [2, p-1] a: '))
ha = pow(g, a, p)
print('Public key ha = g^a mod p = ', ha)

uInput = ""
while not uInput.startswith('q'):
    uInput = input("\nPossible options: Encrypt, Decrypt, Sign, Verify and Quit. All inputs must be ints. ").lower()

    if uInput.startswith('e'):
        m = int(input('Cleartext message m: '))
        if m > p:
            print('m should be in the group F_p, i.e. m < p.')
            exit(1)

        k = input('Random Nonce k, or Generate one ([k] / G): ')
        if k.lower().startswith('g'):
            k = random.randint(2, p)
        else:
            k = int(k)

        r = pow(g, k, p)
        c = (pow(ha, k, p) * m) % p
        print('Ciphertext message: h_a * m mod p = ', c, 'Partial decryption key r: ', r)

    elif uInput.startswith('d'):
        c = int(input('Ciphertext message: '))
        r = int(input('Partial decryption key r: '))

        ra = pow(r, -a, p)
        m = (c * ra) % p
        print('Cleartext message: m = c * r^-a mod n = g^ak * m * g^-ka =', m)

    elif uInput.startswith('s'):
        m = int(input('Message to sign (must be hashed due to homomorphism of ElGamal): '))
        l = input('Use large prime factor of p-1 l? ([l] / n): ')
        if l.lower().startswith('n'):
            l = p - 1
        else:
            l = int(l)
            if g > l:
                print('g must be of order l if you use chosen l. See DSA for a generator algorithm')

        while True:
            k = input('Random Nonce k, or Generate one ([k] / G): ')
            if k.lower().startswith('g'):
                k = random.randint(2, l)
                print('k: ', k)
            else:
                k = int(k)
            r = pow(g, k, p)
            try:
                k_inv = pow(k, -1, l)  # may crash the program if inverse does not exist: if it does, use l option above
                break
            except ValueError:
                print('This k was not invertable. Trying again.')
                continue
        s = (k_inv * (m + a * r)) % l

        print('Signature s = k^-1 * (m + a*r) with r = g^k. (r, s) = ( ' + str(r) + ', ' + str(s) + ')')

    elif uInput.startswith('v'):
        m = int(input('Hashed message to verify (must be hashed due to homomorphism of ElGamal): '))
        r = int(input('r: '))
        s = int(input('s: '))

        r_s = pow(r, s, p)
        check = (pow(g, m, p) * pow(ha, r, p)) % p
        print(r_s, check)
        print('Verify r^s = g^m * ha^r (mod p) : ', r_s == check)
