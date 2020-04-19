a,b=map(int,input().split())

if a==b:
    print((str(a)+'1'),(str(b)+'2'))
elif a<b and b-a==1:
    print((str(a)+'9'),(str(b)+'0'))
elif a==9 and b==1:
    print(9,10)
else:
    print(-1)
        
