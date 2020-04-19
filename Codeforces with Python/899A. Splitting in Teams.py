n=int(input())
a=list(map(int,input().split()))
one=a.count(1);two=n-one
if one==two:print(one)
elif one>two:one=one-two;print(two+(one//3))
else:print(one)
