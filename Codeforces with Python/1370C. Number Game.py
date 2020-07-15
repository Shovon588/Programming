from math import sqrt

for I in range(int(input())):
    n = int(input())

    if n==1:
        print('FastestFinger')
    else:
        count=0
        while(1):
            if n%2==1 or n==2:
                if count%2==0:
                    print('Ashishgup')
                else:
                    print('FastestFinger')
                break
            else:
                flag=''
                for i in range (int(sqrt(n))+1,2,-1):
                    if n%i==0:
                        
                        temp1 = i
                        temp2 = -1

                        if (n//temp1)%2==1:
                            temp2 = n//temp1

                        if temp1>=temp2:
                        
                            if temp1%2==1 and (n//temp1)%2==0 and (n//temp1)>2:
                                n = n//temp1
                                flag='done'
                                break
                            
                            if temp2>0 and (n//temp2)%2==0 and (n//temp2)>2:
                                n = n//temp2
                                flag='done'
                                break
                        else:
                            if temp2>0 and (n//temp2)%2==0 and (n//temp2)>2:
                                n = n//temp2
                                flag='done'
                                break
                            if temp1%2==1 and (n//temp1)%2==0 and (n//temp1)>2:
                                n = n//temp1
                                flag='done'
                                break
                        
                if flag=='':
                    n = n-1
                    
                count+=1
