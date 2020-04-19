a=int(input())

b=int(a**0.5)

c = range(1, a+1)
while(len(c)>b):
  for i in c[-b:]:
    print(str(i))
  c=c[:-b]

print(c)
for i in c:
  print(str(i))
