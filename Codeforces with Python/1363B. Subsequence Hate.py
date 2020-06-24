def mismatch(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count

for I in range(int(input())):
    s = input()

    l = len(s)
    zeros = s.count('0')
    ones = s.count('1')
    zero = 0
    one = 0
    res = 100000055
    for char in s:
        if char=='0':zero+=1
        else:one+=1
        
        res = min(res, zero+ones-one)
        res = min(res, one+zeros-zero)
    print(res)
