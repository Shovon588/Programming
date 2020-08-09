s = input()

dic = {}
value_count = {}

for char in s:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1


for key,value in dic.items():
    if value in value_count:
        value_count[value]+=1
    else:
        value_count[value]=1

