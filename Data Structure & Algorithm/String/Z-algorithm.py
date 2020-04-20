s='aabxaabxcaabxaabxay'

left=0;right=1;count=0
z=[0]

while(right<len(s)):
    if s[left]==s[right]:
        left+=1;right+=1
        count+=1
    else:
        print(right)
        z.append(count)
        if left!=0:
            l=right-count;r=right-1;temp=l+1
            
            for i in range(1,count):
                if z[i]+temp>r:
                    pass
                else:
                    z.append(z[i])
                    temp+=1
                    
            left=0;count=0;
        else:
            right+=1

if left>0:
    z.append(left)
