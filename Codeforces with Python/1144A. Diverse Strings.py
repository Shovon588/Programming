check=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(int(input())):
     s=input()
     a=''.join(set(s))
     if len(a)!=len(s):
          print('No')
     else:
          a=list(a)
          a.sort()
          temp=a[0]

          flag=check.index(temp)
          count=0
          for j in range(len(a)):
               if a[j]==check[flag]:
                    count+=1;flag+=1
               else:
                    break
          if count==len(a):
               print('Yes')
          else:
               print('No')
