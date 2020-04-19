def PrevPal(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x

def NextPal(a):
    lena=len(a)//2
    head=a[:lena]

    if head+head[::-1]>a:
        return(head+head[::-1])
    else:
        while head+head[::-1]<=a:
            head=str(int(head)+1)
        return(head+head[::-1])

t=int(input())
for i in range(t):
    a=input()
    if a==a[::-1]:
        print(a)
    else:
        b=PrevPal(int(a))
        c=int((NextPal(a)))
        l=abs(int(a)-b)
        m=abs(int(a)-c)

        if l>m:
            print(c)
        else:
            print(b)
                
        
