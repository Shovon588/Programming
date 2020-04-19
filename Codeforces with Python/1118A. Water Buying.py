for i in range(int(input())):
     n,a,b=map(int,input().split())
     temp1=n*a
     
     if n%2==0:
          temp2=(n//2)*b
     else:
          temp2=((n//2)*b)+a
     print(min(temp1,temp2))
