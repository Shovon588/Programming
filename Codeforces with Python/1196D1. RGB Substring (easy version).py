t='RGB'

for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    res=2005;

    for i in range(n-k+1):
        temp=t.index(s[i]);count=0
        
        for j in range(i,i+k):
            if s[j]==t[temp]:
                pass
            else:
                count+=1
                
            if temp==2:
                temp=0
            else:
                temp+=1

        if count<res:res=count
    print(res)
