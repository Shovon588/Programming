n = int(input())
a=[];flag='y';pre='';
for i in range(n):
    new=input()
    if new in a:
        print('No')
        flag='n'
        break

    if i>0:
        if new[0]!=pre[len(pre)-1]:
            print('No')
            flag='n'
            break
    a.append(new)
    pre=new

if flag=='y':
    print('Yes')
        
