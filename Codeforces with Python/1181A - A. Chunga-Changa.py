x,y,z=map(int,input().split())

result=(x//z)+(y//z)

temp1,temp2=min((x%z),(y%z)),max((x%z),(y%z))

if(temp1+temp2)>=z:
     result+=1
     print(result,temp1)
else:
     print(result,0)
