for I in range(int(input())):
    n = int(input())
    s = input()

    left = 0
    right = 0
    res = 0
    for i,char in enumerate(s):
        if char=='(':
            left+=1

        if char==')':
            if left<=right:
                res+=1
            else:
                right+=1

    print(res)
        
    
