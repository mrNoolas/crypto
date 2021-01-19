
print("Schoolbook RSA\n\n")

p = int(input('p: '))
q = int(input('q: '))
n = p * q
print('n = p*q = ', n)

print('Watch it: gcd(e, (p-1)(q-1)) must be 1!')
e = int(input('e: '))
d = pow(e, -1, (p - 1) * (q - 1))
print('d = e^-1 mod (p-1)(q-1) = ', d)
print('Private Key is (d, n); Public key is (e, n).')

uInput = ""
while not uInput.startswith('q'):
    uInput = input("Possible options: Encrypt, Decrypt, Sign and Quit. All inputs must be ints. ").lower()

    if uInput.startswith('e'):
        m = int(input('Cleartext message: '))
        c = pow(m, e, n)
        print('Ciphertext message: m^e mod n = ', c)

    elif uInput.startswith('d'):
        c = int(input('Ciphertext message: '))
        m = pow(c, d, n)
        print('Cleartext message: c^d mod n = ', m)

    elif uInput.startswith('s'):
        print('Make sure to hash m to reduce its input size to <n and to improve security from oracle attacks!')
        m = int(input('Message to sign: '))
        s = pow(m, d, n)
        print('Signature: m^d mod n = ', s)
