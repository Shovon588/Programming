vows = ['a', 'e', 'i', 'o', 'u']

for I in range(int(input())):
    n = int(input())
    s = input().lower()
    t = input().lower()

    

    first = 0
    second = 0

    for char in s:
        if char in vows:
            first+=1

    for char in t:
        if char in vows:
            second+=1

    if first>second:
        print("First String")
    elif second>first:
        print("Second String")
    else:
        print("Equal")
        
