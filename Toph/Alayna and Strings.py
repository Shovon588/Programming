lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()

s=input()

l=0;u=0
for char in s:
    if char in lower:l+=1
    elif char in upper:u+=1

print(u,l)
