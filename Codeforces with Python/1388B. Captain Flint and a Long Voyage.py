for I in range(int(input())):
    n = int(input())
    needed = (n*4)-n
    nine = needed//4
    rem = needed%4

    result = nine*'9'

    '''
    if rem>0:
        maxi = -1
        res = -1
        for i in range(10):
            temp = '000' + bin(i)[2:]
            temp = temp[-4:]
            
            if int(temp[:rem])>maxi:
                maxi = int(temp[:rem])
                res = i
            
        result+=str(res)
    '''
        
    for i in range(n-len(result)):
        result+='8'

    print(result)
