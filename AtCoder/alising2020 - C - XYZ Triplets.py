n = int(input())
ans = [0]*(n+5)

for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            temp = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if n>=temp:
                print(x,y,z, temp)
                ans[temp]+=1


for i in range(1,n+1):
    print(ans[i])
