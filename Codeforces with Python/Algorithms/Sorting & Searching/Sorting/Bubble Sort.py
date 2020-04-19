n=int(input())
a=list(map(int,input().split()))

def bubble(arr,n):
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
            print(a)
    return arr

print('Normal bubble result:',bubble(a,n))

#Time complexity = O(n^2) - always



def Optimized_bubble(a,n):
    swap=False
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]
                swap=True
            print(a)
        if swap==False:
            break
    return a

print('Optimized bubble reseult:',Optimized_bubble(a,n))

#Time complexity = O(n) - best case, otherwise O(n^2)


#For more: https://www.geeksforgeeks.org/bubble-sort/
