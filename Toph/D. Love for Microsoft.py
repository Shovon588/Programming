s =  input()

result = "We both love Microsoft!"
req = "microsft"

for char in req:
    if char not in s:
        result = "Only I love Microsoft!"
        break

print(result)
    
