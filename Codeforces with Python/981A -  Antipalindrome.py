a = input()
b = a[::-1]

c = ''.join(set(a))

if a==b and len(c)==1:
    print ('0')
elif a==b:
    print (len(a)-1)
else:
    print (len(a))
