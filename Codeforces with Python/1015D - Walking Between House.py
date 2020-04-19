n,k,s = map(int,input().split())
temp = n-1
check=[]
flag=1

if k>s or (n*k)<s:
    print('NO')
    flag=0
else:
    while(1):
        if s-temp>=k:
            s=s-temp
            check.append(temp)
            k-=1
            if k==0:
                break
        else:
            break



if k==0:
    flag=0
    print('NO')
else:
    check.append(s-(k-1))
    s=s-k
    k-=1

    
for i in range(k):
    check.append(1)

initial=1
if flag!=0:
    print('YES')
    for i in range(len(check)):
        if check[i]==temp:
            if initial==1:
                print(n,end=' ')
                initial=n
            elif initial==n:
                print(1,end=' ')
                initial=1
                
        elif check[i]==1:
            if initial+1>n:
                print(initial-1,end=' ')
                initial-=1
            else:
                print(initial+1,end=' ')
                initial+=1

        else:
            if initial+check[i]>n:
                print(initial-check[i],end=' ')
                initial-=check[i]
            else:
                print(initial+check[i],end=' ')
                initial+=check[i]

            
                

                
