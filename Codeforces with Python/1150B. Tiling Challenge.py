n=int(input())
a=[[0 for i  in range(n)]for j in range(n)]

for i in range(n):
     s=input()
     for j in range(n):
          a[i][j]=s[j]

for i in range(n):
     for j in range(n):
          if i-1>=0 and i+1<n and j-1>=0 and j+1<n:
               if a[i][j]=='.' and a[i-1][j]=='.' and a[i+1][j]=='.' and a[i][j-1]=='.' and a[i][j+1]=='.':
                    a[i][j]='#';a[i-1][j]='#';a[i+1][j]='#';a[i][j-1]='#';a[i][j+1]='#'
          else:
               pass

flag=''
for i in range(n):
     if '.' in a[i]:
          print('NO')
          flag='no'
          break
if flag=='':
     print('YES')
