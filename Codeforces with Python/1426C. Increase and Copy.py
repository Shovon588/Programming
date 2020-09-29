from math import sqrt, ceil

for I in range(int(input())):
    n = int(input())

    mini = 1000000000000
    num = -1
    it = int(sqrt(n))+1
    for i in range(it, max(0,it-5), -1):
        cost = i-1
        temp = n-i
        rem = ceil(temp/i)

        tot = cost + rem
        mini = min(mini, tot)

    print(mini)
