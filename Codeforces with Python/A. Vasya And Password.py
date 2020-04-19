t=int(input())
for i in range(t):
    big=0;small=0;dig=0;
    s=input()
    lens=len(s)

    for j in range(lens):
        if s[j]>='A' and s[j]<='Z':
            big+=1
        elif s[j]>'a' and s[j]<='z':
            small+=1
        elif s[j]>='0' and s[j]<='9':
            dig+=1

    if small==0 and dig==0:
        a='a1'+s[2:]
    elif big==0 and dig==0:
        a='A1'+s[2:]
    elif big==0 and small==0:
        a='Aa'+s[2:]
    print(a)
