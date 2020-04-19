n=int(input())
s=input()

letter='abcdefghijklmnopqrstuvwxyz'

for i in s:
    if i in letter:
        ind=letter.index(i)
        print(letter[ind-n],end='')
    else:
        print(i,end='')
