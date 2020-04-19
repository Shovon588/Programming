n=int(input())

a={}
for i in range(n):
    s=input()
    if s in a:
        a[s]+=1
        print(s+str(a[s]))
    else:
        print('OK')
        a[s]=0
