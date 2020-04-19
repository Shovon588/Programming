n = int(input())
s = input()


pos = 0
preTrig = 'ground'
count = 0
for char in s:
    if char=='U':
        pos+=1
    else:
        pos-=1

    if pos>0:
        trig = 'mountain'
    elif pos==0:
        trig = 'ground'
    else:
        trig = 'valley'

    if preTrig=='valley' and trig=='ground':
        count+=1

    preTrig = trig
