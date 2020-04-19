n = input()

a=int(n)
for i in range(a+1,a+1000):
    b=str(i)
    c=''.join(set(b))

    if len(c)==4:
        print(b)
        break
