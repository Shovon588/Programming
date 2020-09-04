for I in range(int(input())):
    a,b = map(int,input().split())

    diff = abs(a-b)
    temp = diff//10

    if diff%10==0:
        print(temp)
    else:
        print(temp+1)
