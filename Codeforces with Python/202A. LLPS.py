letters = 'abcdefghijklmnopqrstuvwxyz'

s = input()

res = -1
for char in s:
    index = letters.index(char)
    res = max(res,index)

count = s.count(letters[res])

print(letters[res]*count)
