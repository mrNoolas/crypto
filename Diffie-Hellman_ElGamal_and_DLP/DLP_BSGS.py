
import math


def BinarySearch(lys, val):
    """ Use lys with a list of tuples, where the first value of the tuple is the one to search on."""
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid][0] == val:
            index = mid
        else:
            if val < lys[mid][0]:
                last = mid - 1
            else:
                first = mid + 1
    return index

print('Solving DLP - Baby Step Giant Step\n\n')

# Get the parameters to break:
p = int(input('Number that defines the multiplicative group p: '))
l = int(input('Subgroup defined by l: '))
g = int(input('Generator of the group g: '))
ha = int(input('Challenge ha for which to find log_g ha = a; ha: '))

m = math.floor(math.sqrt(l))
G = []
for i in range(0, m):
    G.append(((g ** i) % p, i))

G.sort(key=lambda g_i: g_i[0])


for j in range(0, math.ceil(math.sqrt(l))):
    probe = (ha * pow(g, -m*j, p)) % p
    index = BinarySearch(G, probe)
    if index != -1:
        print('a = i + mj = ' + str(G[index][1]) + ' + ' + str(m) + ' * ' + str(j) + ' = ' + str(G[index][1] + m*j))
        break

