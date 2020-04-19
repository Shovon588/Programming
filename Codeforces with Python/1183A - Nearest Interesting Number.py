s=input()

while(1):
     total=0
     for i in s:
          total+=int(i)

     if total%4==0:
          print(s)
          break
     else:
          s=str(int(s)+1)
