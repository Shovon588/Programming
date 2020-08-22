s =  input()

req = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 26
for char in req:
    if char in s:
        result-=1

print(result)
