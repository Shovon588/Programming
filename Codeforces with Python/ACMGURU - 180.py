n = int (input())
count=0
a = list (map(int,input().split()))
print (a)
for j in range(len(a)):
    b = [i for i in a if i<a[j]]
    a.remove(a[j])
