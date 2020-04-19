for _ in range(int(input())):
    n=int(input())
    temp=(n-1)//2

    if n<=4:
        print(4-n)
    else:
        print(2*(1+temp)-n)
