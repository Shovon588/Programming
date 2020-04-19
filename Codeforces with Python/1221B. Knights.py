n=int(input())

bFirst='BW'*((n//2)+1)
wFirst='WB'*((n//2)+1)

for i in range(n):
    if i%2==0:
        print(bFirst[:n])
    else:
        print(wFirst[:n])
