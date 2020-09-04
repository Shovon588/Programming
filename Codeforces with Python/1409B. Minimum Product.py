for I in range(int(input())):
    a,b,x,y,n = map(int,input().split())

    diffa = a-x
    diffb = b-y

    possible_a = max(x,a-n)
    possible_b = max(y,b-n)

    if possible_a>=possible_b:
        # work with b
        cost = b-possible_b
        first_num = possible_b
        second_num = a
        tag = 'a'
    else:
        #work with a
        cost = a-possible_a
        first_num = possible_a
        second_num = b
        tag='b'

    rem_n = n-cost
    if tag=='a':
        second_num = max(x,second_num-rem_n)
    else:
        second_num = max(y,second_num-rem_n)

    print(first_num*second_num)
    
        
