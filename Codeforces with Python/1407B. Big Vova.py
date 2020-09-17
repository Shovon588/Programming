from math import sqrt

def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 

	return x 

def find_divisors(n):
    divs = []
    for i in range(1,int(sqrt(n))+2):
        if n%i==0:
            if i!=n//i:
                divs.append(n//i)
                divs.append(i)
            else:
                divs.append(i)

    for i in range(2,1000):
        if n*i>first:
            break
        divs.append(n*i)
        
    divs.sort(reverse=True)
    return divs
    

for I in range(int(input())):
    nums = {}
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)

    first = a[0]
    gcd = first
    
    for num in a:
        if num in nums:
            nums[num]+=1
        else:
            nums[num]=1

    print(first,end=' ')
    nums[first]-=1

    found=True
    while gcd>1 and found:
        divs = find_divisors(gcd)
        found=False
        for div in divs:
            if div in nums:
                if nums[div]>0:
                    nums[div]-=1
                    gcd=find_gcd(gcd,div)
                    print(div,end=' ')
                    found=True

        if not found:
            flag = -1
            temp_num = -1
            for num in nums:
                if nums[num]>0:
                    temp = find_gcd(gcd,num)
                    if temp>flag:
                        flag=temp
                        temp_num=num

            if temp_num!=-1:        
                print(temp_num,end=' ')
                nums[temp_num]-=1
                gcd = find_gcd(gcd,temp_num)
                found=True


    for num in nums:
        if nums[num]>0:
            for i in range(nums[num]):
                print(num,end=' ')

    print()








    
    
