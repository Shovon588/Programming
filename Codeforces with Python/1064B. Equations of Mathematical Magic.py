for i in range(int(input())):
    a=int(input())
    b=bin(a)
    c=b.count('1')
    print(2**c)
