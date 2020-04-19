a,b=input(),input()
count=0
for i in range (len(a)):
    if a[i]==b[i]:
        count+=1

c = set (a) & set (b)
c= len(c)
c=c-count

print (count,c)
