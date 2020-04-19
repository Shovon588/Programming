vow=['a','e','i','o','u']

s=input()
t=input()

ls=len(s)
lt=len(t)
count=0
if ls!=lt:
    print('No')
else:
    for i in range(ls):
        if (s[i] in vow and t[i] in vow) or (s[i] not in vow and t[i] not in vow):
            count+=1

    if count==ls:
        print('Yes')
    else:
        print('No')
