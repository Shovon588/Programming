t=int(input())
for _ in range(t):
    temp=0;yo=0;
    n=int(input())
    for i in range(n):
        s=list(map(int,input().split()))

        if len(s)==1:
            yo+=s[0]
            temp=0
        elif temp==0:
            if s[temp]>=s[temp+1]:
                yo+=s[temp]
                print(s[temp],yo)
            else:
                yo+=s[temp+1]
                print(s[temp],yo,'here')
                temp=temp+1
        elif len(s)-1==temp:
            yo+=s[temp-1]
            print(s[temp],yo,'overhere')
            temp-=1
            
