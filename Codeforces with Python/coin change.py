coin=[2,4]

possible=[0 for i in range(36)]
possible[0]=1

for i in range(1,36):
    for j in range(2):
        if i>=coin[j]:
            possible[i]|=possible[i-coin[j]]
