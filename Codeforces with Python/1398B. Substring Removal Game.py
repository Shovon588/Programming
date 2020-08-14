for I in range(int(input())):
    s = input()

    ones = []

    one = 0
    for char in s:
        if char=='1':
            one+=1
        else:
            ones.append(one)
            one=0
    if one>0:
        ones.append(one)

    if len(ones)>0:
        ones.sort(reverse=True)
        res=0
        for i in range(0,len(ones),2):
            res+=ones[i]

        print(res)
    else:
        print(0)
