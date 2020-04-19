t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    temp=a
    c=((a-b)/a)*100
    if c<=25:
        print(0)
    else:
        while(1):
            a+=1;b+=1
            c=((a-b)/a)*100
            if c<=25:
                print(a-temp)
                break
