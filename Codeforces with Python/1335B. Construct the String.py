let = "abcdefghijklmnopqrstuvwxyz"

for _ in range(int(input())):
    n,a,b = map(int,input().split())

    substr = n-a

    initial = let[:b]
    initial = initial*((a//b)+1)
    initial = initial[:a]

    print(initial,end='')

    index=0
    for i in range(substr):
        print(initial[index],end='')
        index+=1

        if index>=a:
            index=0
    print()
