for I in range(int(input())):
    s = input()
    
    tot = 0
    dic = {}
    for i,char in enumerate(s):
        if char == '+':
            tot+=1
        else:
            tot-=1

        if tot<0:
            if tot not in dic:
                dic[tot]=[i+1]
            else:
                dic[tot].append(i+1)


    res = 0
    for init in range(10):
        cur = init
        ok = True

        for char in s:
            print(init,cur,res)
            res+=1
            if char=='+':
                cur+=1
            else:
                cur-=1

            if cur<0:
                ok = False
                break
        if ok:
            break

    print(res)
    
            
