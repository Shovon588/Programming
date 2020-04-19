t=int(input())
for _ in range(t):
    c,m,s=map(int,input().split())

    result=0

    result=min(c,m,s)
    c,m=c-result,m-result

    mini,maxi=min(c,m),max(c,m)

    if maxi//2>=mini:
        result+=mini
    else:
        result+=maxi-mini
        maxi,mini=maxi-(maxi-mini)*2,mini-(maxi-mini)

    if mini==maxi:
        result+=(mini+maxi)//3

    print(result)
