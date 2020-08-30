s = input()
t = input()

lens = len(s)
lent = len(t)

total = 100000000
for i in range(lens-lent+1):
    count = 0
    for j in range(lent):
        if s[i+j]!=t[j]:
            count+=1
    total = min(total,count)
    print(s[i:i+lent])

if total == 100000000:
    print(lent)
else:
    print(total)
            
