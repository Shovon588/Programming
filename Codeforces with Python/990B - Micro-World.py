n,m=map(int,input().split())

l,j = sorted(map(int, input().split())), 0


for a in l:
    while l[j] < a:
        if a <= l[j] + m:
            n -= 1
        j += 1

print(n)



