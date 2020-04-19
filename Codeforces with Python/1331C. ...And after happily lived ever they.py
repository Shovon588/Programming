n = int(input())

bi = list(((6-len(bin(n)[2:]))*'0')+bin(n)[2:])

bi[1],bi[5] = bi[5], bi[1]
bi[2],bi[3] = bi[3], bi[2]

bi = ''.join(bi)

print(int(bi,2))
