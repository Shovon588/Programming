s=input()

temp=s.count('a')

if temp*2>len(s):
     print(len(s))
else:
     print((2*temp)-1)
