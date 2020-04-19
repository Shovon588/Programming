
dic={}
def fun(x):
    if x==1:return 1

    if x%2==0:
        try:
            if dic[x]:
                return dic[x]
        except KeyError:
            dic[x]=((fun(x//2)*fun(x//2))+1)%18446744073709551616
            return dic[x]

    else:
        try:
            if dic[x]:
                return dic[x]
        except KeyError:
            dic[x]=((fun(x//2)*fun((x//2)+1))+2)%18446744073709551616
        return dic[x]




for i in range(int(input())):
    n=int(input())
    s=str(fun(n))

    print("Case %d: %s"%(i+1,s))
