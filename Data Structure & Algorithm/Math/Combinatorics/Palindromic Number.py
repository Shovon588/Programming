                                            #############################################
                                            ##How to find a palindrome number???##
                                            #############################################


a=input()

##input ta jodi ekta digit er hoy (ex: 1,2,6,9 etc) tahole just input er sathe 1 add hoia jabe
if len(a)==1 and a!='9':
    print(int(a)+1)

#input a jodi sobgula 9 thake (ex: 9,99,9999 etc) tahole just input er sathe 2 add hoia jabe
elif ''.join(set(a))=='9':
    lena=len(a)
    print(int(a)+2)

#uporer case duita jodi na hoy tahole case thake 2 ta...odd length er input r even length er input
else:
    
    #input ta jodi even length er hoy tahole input er ordhek head er moddhe rakhbo
    if len(a)%2==0:
        lena=len(a)//2
        head=a[:lena]

        #jodi head+reverse(head) input er theke boro hoy taile head+reverse(head) print korbo
        if head+head[::-1]>a:
            print(head+head[::-1])
        #na hole joto somoy head+head(reverse) input er theke boro na hoy toto somoy head 1 kore boro korbo
        else:
            while head+head[::-1]<=a:
                head=str(int(head)+1)
            print(head+head[::-1])
            
    #input jodi odd length er hoy tahole first half head er moddhe r middle digit mid er moddhe rakhbo
    else:
        lena=len(a)//2
        head=a[:lena]
        mid=a[lena]

        #ebar jodi head+mid+reverse(head) input er theke boro hoy tahole head+mid+reverse(head) print korbo
        if head+mid+head[::-1]>a:
            print(head+mid+head[::-1])
        #jodi na hoy taile joto somoy head+mid+reverse(head) input er theke boro  na hoy toto somoy 1 kore add korbo
        #ekhane mid er value ek kore barte barte jodi 10 hoia jai tahole head a 1 add korbo r mid=0 kore dibo
        else:
            while head+mid+head[::-1]<=a:
                mid=str(int(mid)+1)
                if mid=='10':
                    head=str(int(head)+1)
                    mid='0'
            print(head+mid+head[::-1])



#To find previous palindromic number
def Previous_Palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
        
print(Previous_Palindrome(int(a)))

                                                            ###########
                                                            ##THE END##                 
                                                            ###########
