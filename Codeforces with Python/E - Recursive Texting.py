t=int(input())

num=[0,1,2,3,4,5,6,7,8,9]
letter=['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
dig=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

for z in range(t):
    s,n,k=input().split()
    n,k=int(n),int(k)
    for i in range(n):
        a=''
        lens=len(s)
        for j in range(lens):
            for l in range(10):
                if s[j] in letter[l]:
                    a=a+dig[l]
                    ##print(a)
        s=a[::1]
    print('Case ',z+1,':',s[k-1])

                    
