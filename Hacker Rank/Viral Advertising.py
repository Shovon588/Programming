n = int(input())

initial = 5
total = 0
for i in range(n):
    liked = initial//2
    total+=liked
    initial = liked*3

    print(initial,liked,total)
