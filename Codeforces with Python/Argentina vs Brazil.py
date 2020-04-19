t=int(input())

while(t>0):
    n,m=input().split()
    n,m=int(n),int(m)

    if n>m:
        print("Argentina ",n," - ",m," Brazil")
    elif m>n:
        print("Brazil ",m," - ",n," Argentina")

    t-=1
