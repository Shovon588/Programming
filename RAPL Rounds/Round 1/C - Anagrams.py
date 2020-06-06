def fact(n):
    num=1
    for i in range(1,n+1):
        num=num*i
    return num

s=input()

dic={}
for char in s:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1

res = fact(len(s))

for key in dic:
    res = res//fact(dic[key])

print(res)
