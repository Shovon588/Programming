s = input()

res = 0

rainy = 0
for char in s:
    if char=='R':
        rainy+=1
    else:
        res = max(res,rainy)
        rainy=0

res = max(res,rainy)

print(res)
