thres = 1000000000000000000

#log(b)
def power(a,b):
    result = 1
    while b>0:
        if b%2==1:
            result = result * a
            if result>thres:
                return -1

        a = a*a
        b = b//2
        
    return result


#log2(n)*log2(n)
def bin_search():
    low = 2
    high = last

    while low<high:
        mid = (low+high)//2

        temp = power(mid,n-1)
        if temp>last or temp==-1:
            high = mid-1
        else:
            low=mid+1
            
    return low,high


#O(n)*log(n)
def calculate(num):
    res = 0
    for i in range(n):
        temp = abs(a[i]-power(num,i))
        res+=temp
    return res


n = int(input())
a = list(map(int,input().split()))#O(n)
a.sort()

last = a[-1]

#log2(n)
first,second = bin_search()


#O(4n) - max
result = thres
for i in range(second-1,first+2):
    temp = calculate(i)
    result = min(result,temp)

print(result)





