n=int(input())
a=list(map(int,input().split()))

a.sort()
tempa=a[-1]-a[1]
tempb=a[-2]-a[0]

print(min(tempa,tempb))
