for _ in range(int(input())):
    money=[];friend=[]
    n,m=map(int,input().split())
    for i in range(n):
        tk=int(input())
        money.append(tk)

    for i in range(m):
        f1,f2=map(int,input().split())
        friend.append((f1,f2))

    friend.sort()

    for i in range(m):
        f1,f2=friend[i][0],friend[i][1]
        print(f1,f2)
    
