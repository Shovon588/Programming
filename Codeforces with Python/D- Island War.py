n, m = map(int, input().split())
disputes = []
for i in range(m):
    a, b = map(int, input().split())
    disputes.append((b, a))

disputes.sort()
print(disputes)
ans=0
flag=0
for b,a in disputes:
    if flag<=a:
        ans+=1
        flag=b
        

print(ans)

        
