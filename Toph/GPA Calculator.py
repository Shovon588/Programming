for i in range(int(input())):
    n=int(input())
    total=0
    for j in range(n):
        m=float(input())
        total+=m

    res = total/n

    print('Case %d: %.3f' %(i+1,res))
