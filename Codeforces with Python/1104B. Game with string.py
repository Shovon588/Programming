s=input()
s=list(s)

i=1
while(1):
    check=0
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            s.remove(s[j])
            s.remove(s[j])
            check=1
            break
            
    if check!=1:
        if i%2==0:
            print('Yes')
        else:
            print('No')
        break
    
    else:i+=1    
