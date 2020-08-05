def find_and_update(n):
    pass


for I in range(int(input())):
    n = int(input())
    s = input()

    arr = [-1 for i in range(n)]
    
    zeros = []
    ones = []

    for i,char in enumerate(s):
        if char=='1':
            ones.append(i)
        else:
            zeros.append(i)
