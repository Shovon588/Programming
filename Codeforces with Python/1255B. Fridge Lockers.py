for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))

    l=[]
    for i in range(n):
        l.append((a[i],i+1))
    l.sort()
    
    cost=0;res=[]
    check=[0 for i in range(n+1)]
    flag=[[0 for i in range(n+1)]for j in range(n+1)]
    
    if m<n:
        print('-1')
    else:
        for i in range(n):
            temp=i+1;left=0
            while(check[temp]<2):
                if l[left][1]!=temp:
                    if flag[temp][l[left][1]]==0 and check[l[left][1]]<2:
                        cost+=a[temp]+l[left][0]
                        
                        flag[temp][l[left][1]]=1
                        flag[l[left][1]][temp]=1
                        check[temp]+=1
                        check[l[left][1]]+=1

                        print(temp,l[left][1])
                        left+=1
                    else:
                        left+=1
                else:
                    left+=1
                        
