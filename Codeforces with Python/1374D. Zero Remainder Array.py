for I in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
 
    dic = {}

    for i,num in enumerate(a):
        a[i] = num%k

    dic = {}
    flag = False
    for i,num in enumerate(a):
        if num==0:
            continue
        flag = True
        
        if num in dic:
            dic[num]+=k
        else:
            dic[num]=k-num

    if not flag:
        print(0)
    else:
        print(max(dic.values())+1)
