z=int(input())
for zz in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    temp=[0]*(n+1)

    for i in range(n):
        temp[a[i]]+=1
        
    temp.sort(reverse=True)

    last=temp[0]+1;res=0
    
    for i in temp:
        last=max(min(last-1,i),0)
        res+=last
    print(res)
