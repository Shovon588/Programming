from math import log2,ceil

while(1):
    try:
        n=int(input())+1

        n=ceil(log2(n))
        print(n)
    except EOFError:
        break
