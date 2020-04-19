from math import sqrt as sq, ceil

s = input()
s = s.replace(' ','')

l = sq(len(s))
row = int(l)
col = ceil(l)

if row*col<len(s):
    row+=1

ini = 0
trans = []
for i in range(row-1):
    trans.append(s[ini:ini+col])
    ini = ini+col
trans.append(s[ini:])

result = []
for i in range(col):
    res=''
    for word in trans:
        try:
            res+=word[i]
        except IndexError:
            pass
    result.append(res)
    
