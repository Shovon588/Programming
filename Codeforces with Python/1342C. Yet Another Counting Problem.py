from math import gcd, ceil

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm


for _ in range(int(input())):
    a,b,q = map(int,input().split())

    '''
    for i in range(q):
        l,r = map(int,input().split())
        count=0
        yes = []
        no = []
        for x in range(l,r+1):
            if (x%a)%b!=(x%b)%a:
                count+=1
                yes.append(x)
            else:
                no.append(x)
                
        print(count)'''
    

    for i in range(q):
        count=0
        l,r = map(int,input().split())
        Lcm = lcm(a,b)
        left = ceil(l/Lcm)
        right = int(r/Lcm)

        if r<b:
            print(0,end=' ')
        else:
            if left==1:
                count+=b-1
            else:
                count+=b

            # Right
            if (right*Lcm)+b<=r:
                count+=b
            else:
                count+=max(0,r-(right*Lcm))
                right-=1
            
            
            count=count+max(0,(right-left)*b)

            print(r-l-count+1,end=' ')
    print()






            
