for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    tempdic = {}

    if n>1:
        for num in a:
            if num not in tempdic:
                tempdic[num]=1
            else:
                tempdic[num]+=1

        start = a[0]+a[1]
        end = a[-1]+a[-2]

        result = 0
        
        for lookfor in range(start,end+1):
            dic = tempdic.copy()
            
            count = 0
            for i in range(n):
                if a[i]>=lookfor:
                    break

                temp = lookfor - a[i]
                
                if temp==a[i]:
                    if (temp in dic) and (dic[temp]>=2):
                        count+=1
                        dic[temp]-=2
                else:
                    if (temp in dic) and (dic[temp]>0) and (dic[a[i]]>0):
                        dic[a[i]]-=1
                        dic[temp]-=1
                        count+=1

            result = max(result,count)
            
        print(result)
    else:
        print(0)
