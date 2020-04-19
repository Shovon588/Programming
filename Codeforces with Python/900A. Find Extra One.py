n=int(input())
left=0;right=0

for i in range(n):
    a,b=map(int,input().split())

    if (a>0 and b>0) or (a>0 and b<0) or (a>0 and b==0):
        right+=1

    if (a<0 and b<0) or (a<0 and b>0) or (a<0 and b==0):
        left+=1


if left<=1 or right<=1:
    print('YES')
else:
    print('NO')
