a=input()
b=['ABC','BAC','ACB','BCA','CBA','CAB']
c=0
for i in range(6):
    if b[i] in a:
        c=1
        print('Yes')
        break

if c!=1:
    print('No')
