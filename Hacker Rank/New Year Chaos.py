import sys

for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    dic = {}
    for i,num in enumerate(a):
        dic[num]=i+1
        
    bribe = 0
    flag=''
    for target in range(n,0,-1):
        if abs(dic[target]-target)>2:
            flag = "Too chaotic"
            break
        else:
            if dic[target]-target<0:
                temp = abs(dic[target]-target)
                bribe+=temp
                pos = dic[target]
                if temp==2:
                    dic[a[pos]]-=1
                    dic[a[pos+1]]-=1
                    a[pos-1],a[pos],a[pos+1] = a[pos],a[pos+1],a[pos-1]
                elif temp==1:
                    dic[a[pos]]-=1
                    a[pos-1],a[pos] = a[pos],a[pos-1]

    if flag=='':
        print(bribe)
    else:
        print(flag)
    
"""
2
5
2 1 5 3 4
5
2 5 1 3 4
"""
