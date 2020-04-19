password = input()
weight_a = int(input())


normal = "abcdefghijklmnopqrstuvwxyz"

def getStrength(password, weight_a):
    total = 0
    for char in password:
        index = normal.index(char)
        index = (index+weight_a)%26
        total+=index

    return total


getStrength(password, weight_a)
