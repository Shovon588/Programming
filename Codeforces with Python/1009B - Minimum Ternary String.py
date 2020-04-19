a = input()

b = a.count('1')
a = a.replace('1','')
c = a.find('2')

if c==-1:
    a = (a+ '1'*b)
else:
    a = a[:c]+ '1'*b + a[c:]

print(a)
