for I in range(int(input())):
    n = int(input())
    needed = (n*4)-n
    nine = needed//4
    rem = needed%4

    for i in range(nine):
        print(9,end='')
 
    for i in range(n-nine):
        print(8,end='')

    print()
