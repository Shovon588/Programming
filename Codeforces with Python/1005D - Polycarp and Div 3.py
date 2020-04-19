a = input()

l = len(a)
count = 0

num = ''
for i in range(l):
    b=int(a[i])
    if b==0:
        count+=1
        num=''
        #print(count,b)
    elif b%3==0:
        count+=1
        num=''
        #print(count,b)
    else:
        num+=str(b)
        if ((int(num)%100)%3)==0 or (int(num)%3)==0:
            count+=1
            #print(count,int(num))
            
            num = ''

print(count)
