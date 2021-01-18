
import math

print('Solving DLP - Pollard Rho\n\n')


def step(G, b, c):
    if G % 3 == 0:
        G = (G * g) % p
        b = (b + 1)
        # c = c
    elif G % 3 == 1:
        G = (G * ha) % p
        # b = b
        c = (c + 1)
    else:  # G % 3 == 2:
        G = (G ** 2) % p
        b = (b * 2)
        c = (c * 2)
    return G, b, c


# Get the parameters to break:
p = int(input('Number that defines the multiplicative group p: '))
l = int(input('Subgroup defined by l: '))
g = int(input('Generator of the group g: '))
ha = int(input('Challenge ha for which to find log_g ha = a; ha: '))

G_slow = g
b_slow = 1
c_slow = 0

G_fast = g
b_fast = 1
c_fast = 0

G_slow, b_slow, c_slow = step(G_slow, b_slow, c_slow)
G_fast, b_fast, c_fast = step(G_fast, b_fast, c_fast)
G_fast, b_fast, c_fast = step(G_fast, b_fast, c_fast)

while G_slow != G_fast:
    G_slow, b_slow, c_slow = step(G_slow, b_slow, c_slow)
    G_fast, b_fast, c_fast = step(G_fast, b_fast, c_fast)
    G_fast, b_fast, c_fast = step(G_fast, b_fast, c_fast)

print('a = (b_i - b_j) / (c_j - c_i)  mod l = (b_slow - b_fast) / (c_fast - c_fast) mod l= ' +
      '(' + str(b_slow) + ' - ' + str(b_fast) + ') / (' + str(c_fast) + ' - ' + str(c_slow) + ') mod l = ' )

print('\n\nIf the program crashes, calculate manually...')
numerator = (b_slow - b_fast) % l
denominator = pow(c_fast - c_slow, -1, l)

outcome = (numerator * denominator) % l
print(str(numerator) + ' * ' + str(denominator) + ' mod l = ' + str(outcome))
