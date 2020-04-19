n,k = map(int,input().split())
a = input()

b = a[::-1]
c = ''.join(set(a))

if len(c)!=1 and a!=b:
    print(k*a)
elif len(c)==1:
    print(k*c)
elif a==b:
    print(a+((k-1)*a[1:]))
