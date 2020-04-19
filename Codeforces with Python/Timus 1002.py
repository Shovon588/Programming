import math
a=[]
while(True):
    try:
        n=input()
        for i in n.split():
            b=int(i)
            b=math.sqrt(b)
            a.append(b)
    except EOFError:
        a=a[::-1]
        for i in range(len(a)):
            print("%.4f" %a[i])
        break
