for _ in range(int(input())):
    n = int(input())
    s = input()

    angry = []; res = 0

    s+='A'
    
    for i in range(len(s)):
        if s[i]=='A':
            angry.append(i+1)

    
    for i in range(len(angry)-1):
        res = max(res, angry[i+1]-angry[i]-1)

    print(res)
