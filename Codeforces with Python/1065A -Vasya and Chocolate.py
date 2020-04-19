for i in range(int(input())):
    s,a,b,c=map(int,input().split())
    t=s//c;p=t//a;print(t+(p*b))
