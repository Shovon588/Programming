from sys import stdin, stdout

dic = {0:0, 1:3, 2:6, 3:1, 4:4, 5:7, 6:2, 7:5, 8:8}

#input = stdin.buffer.readline

t = int(input())

for _ in range(t):
    for i in range(9):
        a = list(input())
        index = dic[i]

        if int(a[index])==1:
            a[index] = str(2)
        else:
            a[index] = str(int(a[index])-1)

        print(''.join(a))
            
