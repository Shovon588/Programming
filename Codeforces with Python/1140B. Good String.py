for _ in range(int(input())):
     n=int(input())
     s=input()
     l=n;r=n

     for i in range(n):
          if s[i]=='>':
               l=i
               break
     s=s[::-1]
     for i in range(n):
          if s[i]=='<':
               r=i
               break
     print(min(l,r))
