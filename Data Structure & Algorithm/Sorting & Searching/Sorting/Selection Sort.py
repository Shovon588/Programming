def selection(a,n):
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

n=int(input())
a=list(map(int,input().split()))
print(selection(a,n))


#https://www.geeksforgeeks.org/selection-sort/
#Time complexity O(n^2)
