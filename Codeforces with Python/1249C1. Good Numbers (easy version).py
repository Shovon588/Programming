jinis=[]

for i in range(10):
    jinis.append(pow(3,i))

for _ in range(int(input())):
    n=int(input())
    for i in range(10):
        if jinis[i]>n:
            flag=i-1
            break

    if jinis[flag]==n:
        print(n)
    else:
        if sum(jinis[:flag+1])<n:
            print(jinis[flag+1])
        else:
            count=0
            a=jinis[:flag+1]
            a=a[::-1]
            s=sum(a)
            for i in range(len(a)):
                if n>=a[i]:
                    count+=a[i]
                    n-=a[i]
                    s-=a[i]
                else:
                    if s-a[i]>=n:
                        pass
                    else:
                        count+=a[i]
                        n=0
                        break
            print(count)
                
