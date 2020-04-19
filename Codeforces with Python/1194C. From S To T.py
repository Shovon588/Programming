'''
We have to transform string S to string T.
For this we have to choose one character from P, erase it and
then insert it to string S.

Step 1: We have to clear all character from t which is present in s.
Step 2: We have to clear all character from t which is present in s.


'''


for i in range(int(input())):
     s=list(input())
     t=list(input())
     p=list(input())

     for char in s:
          if char in t:
               t.remove(char)

     for char in p:
          if char in t:
               t.remove(char)

     if len(t)==0:
          print('YES')
     else:
          print('NO')
