for _ in range(int(input())):
    s=input()
    l=len(s)

    start='';end=''
    for i in range(l):
        if s[i]=='1':
            start=i
            break

    for i in range(l-1,-1,-1):
        if s[i]=='1':
            end=i
            break

    count=0
    if start!='' and end!='':
        for i in range(start,end):
            if s[i]=='0':
                count+=1

    print(count)
