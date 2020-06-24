for I in range(int(input())):
    s = input()
    l = len(s)
    
    result = s[:2]

    for i in range(3,l,2):
        result+=s[i]
    print(result)
