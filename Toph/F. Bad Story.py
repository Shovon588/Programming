import math

def num_of_div(n):
    a=[]
    while n%2==0:
        a.append(2)
        n = n//2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            a.append(i)
            n = n//i
                    
    if n>2:
        a.append(n)

    b=list(set(a))
    temp=[]
    for i in b:
        temp.append((i,a.count(i)))


    NOD=1
    for i in range(len(temp)):
        NOD=NOD*(temp[i][1]+1)

    return NOD


n = int(input())
a = list(map(int,input().split()))

numbers = []
for num in a:
    nod = num_of_div(num)
    numbers.append([nod,num])

numbers.sort()

pre = numbers[0][0]

final = {}
for i in range(1,n):
    if numbers[i][0]!=pre:
        final[pre]=numbers[i-1][1]
        pre = numbers[i][0]
        
    numbers[i][1]+=numbers[i-1][1]

if pre not in final:
    final[pre]=numbers[-1][1]


mini = min(final)
for I in range(int(input())):
    n = int(input())

    for i in range(n,-1,-1):
        if i<mini:
            print(0)
            break
        
        if i in final:
            print(final[i])
            break










