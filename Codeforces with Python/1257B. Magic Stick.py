y='yes';n='no'
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==1 and b==1:
        print(y)
    elif a==1 and b>1:
        print(n)
    elif a>b:
        print(y)
    elif a==2 and b>3:
        print(n)
    else:
        t1=a;t2=b;flag='notok';m=0
        for i in range(10):
            if a%2==0:
                a=(3*a)//2
            else:
                a-=1
            if a>=b:
                flag='ok'
            m=max(m,a)

        if flag=='ok':
            print(y)
        elif m-t1>1:
            print(y)
        else:
            print(n)
