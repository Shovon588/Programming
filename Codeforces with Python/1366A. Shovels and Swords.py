for I in range(int(input())):
    s,d = map(int,input().split())
    mini = min(s,d)

    temp = (s+d)//3

    if s>=temp and d>=temp:
        print(temp)
    else:
        print(mini)
