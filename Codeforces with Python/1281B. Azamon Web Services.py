letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(int(input())):
    s,t=map(str,input().split())

    arr = []

    for i,char in enumerate(s):
        temp = letters.index(char)
        arr.append((char,i))
    arr.sort()
    
    flag=''
    for i,char in enumerate(s):
        for j in range(len(s)):
            if arr[j][0]>char:
                break

            if arr[j][0]<char and arr[j][1]>i:
                new = arr[j][1]
                cur = i
                flag='done'
                break
        if flag=='done':
            break
        
