from math import gcd

while True:
    try:
        enc = int(input())
        n = int(input())
        keys = []
        for i in range(n):
            keys.append(int(input()))
        
        prime = 0
        for key in keys:
            prime = gcd(prime,key)
            
        for i in range(n):
            keys[i] = keys[i]//prime

        print("Output: %d" %(enc-sum(keys)))
        blankline = input()

    except:
        break
