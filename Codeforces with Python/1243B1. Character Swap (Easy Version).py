for _ in range(int(input())):
    n=int(input())
    s=input()
    t=input()

    first={};second={};flag='ok'
    for i in range(n):
        if s[i]==t[i]:
            pass
        else:
            flag='notok'
            try:
                if first[s[i]]:
                    first[s[i]]+=1
            except KeyError:
                first[s[i]]=1

            try:
                if second[s[i]]:
                    second[s[i]]+=1
            except KeyError:
                second[s[i]]=1

            
