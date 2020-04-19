n = int(input())
s = input()
t = input()


if sorted(s) != sorted(t):
  print(-1)
else:
  ans = []
  
  for i in range(n):
    a = t[i]
    b = s.index(a)
    print(b)
    for j in range(b,0,-1):
        ans.append((j+i))
    s = s[:b] + s[b+1:]
    print(s)
