s = input()
subS = input()

lens = len(s)
lensubs = len(subS)

count=0
for i in range(lens-lensubs+1):
    if s[i:i+lensubs]==subS:
        count+=1

print(count)
