n,c,m = map(int,input().split())

choco = n//c
wrap = choco

while(1):
    new_wrap = wrap//m
    choco += new_wrap
    wrap = wrap%m
    wrap += new_wrap
    
    if new_wrap==0:
        break
print(choco)
