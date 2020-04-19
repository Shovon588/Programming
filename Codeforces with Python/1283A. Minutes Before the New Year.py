for i in range(int(input())):
    count=0
    h,m=map(int,input().split())

    count+=60-m
    h+=1
    h=24-h
    count+=(h*60)
    
    print(count)

    
