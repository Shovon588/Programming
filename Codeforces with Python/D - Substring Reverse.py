s=input()
t=input()


if s==t:
    print('YES')
else: 
    if len(s)==len(t):
        for i in range(len(s)):
            if s[i]!=t[i]:
                a=i
                break
        for i in range(len(s)-1,-1,-1):
            if s[i]!=t[i]:
                b=i
                break
        sta=s[a:b+1]
        stb=t[a:b+1]


        if len(sta)==len(stb):
            if sta==stb[::-1]:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
    
