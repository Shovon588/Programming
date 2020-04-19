n=int(input())
s=list(input())

count=0
for i in range(0,n,2):
    if s[i]==s[i+1]:
        if s[i]=='a':
            s[i]='b';count+=1
        else:
            s[i]='a';count+=1

print(count)
print(''.join(s))
