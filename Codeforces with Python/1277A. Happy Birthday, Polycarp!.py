for i in range(int(input())):
    s=input()
    n=len(s)
    res = (n-1)*9

    temp = s[0]
    temp = temp*n

    if int(s)>=int(temp):
        res+=int(temp[0])
    else:
        res+=(int(temp[0])-1)

    print(res)
