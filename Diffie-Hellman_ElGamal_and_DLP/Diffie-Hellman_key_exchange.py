
print("Diffie-Hellman key exchange\n\n")

p = int(input('Group order prime p: '))
g = int(input('Generator for F_p g: '))

a = int(input('What is alice\'s secret key? a: '))
ha = pow(g, a, p)
print('ha = ', ha)

bobIsBlackBox = input('Do you want to enter bob\'s pRivate key b or pUblic key hb? (R / U): ').lower().startswith('u')
g_ab = None
if bobIsBlackBox:
    hb = int(input('hb: '))
else:
    b = int(input('b: '))
    hb = pow(g, b, p)
    print('hb = ', hb)

g_ba = pow(hb, a, p)
print('\ng^ba = ', g_ba)
