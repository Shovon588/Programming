a = input()
b = input()
 
lena,lenb = len(a),len(b)
x,y = lena,lenb

i = 0
while(1):
    if a[lena-1]==b[lenb-1] and lena>0 and lenb>0:
        lena-=1
        lenb-=1
        i+=1
    else:
        break

print((x-i)+(y-i))
