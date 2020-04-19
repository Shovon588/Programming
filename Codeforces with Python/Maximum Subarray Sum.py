n=int(input())
a=list(map(int,input().split()))



def algo1(n,a):
    p=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for k in range(i,j):
                s+=a[k]
            p=max(p,s)

    print(p)



#time complexity is O(n^2)
def algo2(n,a):
    p=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=a[j]
            p=max(p,s)
    print(s,p)



#time complexity is O(n)
def algo3(n,a):
    s=0;p=0
    for i in range(n):
        s=max(a[i],s+a[i])
        p=max(s,p)
    print(p)

algo1(n,a)
