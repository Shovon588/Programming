t=int(input())
for i in range(t):
    pointer=0;count=0
    a,b=map(int,input().split())

    if a==100:
        print(1)

    elif a==b or b>a:
        print(-1)
    else:
        while(1):
            pointer+=a
            count+=1
            if pointer>=100:
                print(count)
                break
            pointer-=b
