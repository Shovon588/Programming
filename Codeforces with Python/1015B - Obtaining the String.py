n = int(input())
a = input()
b = input()

a = list(a)
b = list(b)
tempa=a[:]
tempb=b[:]

tempa.sort()
tempb.sort()

count=[];flag=0;
if tempa!=tempb:
    print(-1)
else:
    for i in range(n):
        if a[i]!=b[i]:
            temp=b[i]

            while(a[i]!=b[i]):
                c=a.index(temp)
                a[c-1],a[c]=temp,a[c-1]
                c=a.index(temp)
                count.append(c+1)

                flag+=1
                if flag>=10001:
                    break

    if flag<=10000:
        print(len(count))
        for i in range(len(count)):
            print(count[i],end=' ')
    else:
        print(-1)

print(flag)
