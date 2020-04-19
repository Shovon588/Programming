while(1):
    try:
        l,r=map(int,input().split())
        result=0
        for i in range(min(l,r),max(l,r)+1):
            count=1
            temp=i
            while temp!=1:
                if temp%2==1:
                    temp=(3*temp)+1
                    temp=temp//2
                    count+=2
                else:
                    temp=temp//2
                    count+=1
            if count>result:
                result=count
                
        print(l,r,result)
    except ValueError:
        break
