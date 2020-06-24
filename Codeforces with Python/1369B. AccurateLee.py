for I in range(int(input())):
    n = int(input())
    s = input()

    one = -1
    zero = -1

    for i in range(n):
        if s[i]=='1' and one==-1:
            one=i

        if s[i]=='0':
            zero=i

    if one<0 or zero<0 or one>zero:
        print(s)
    elif one==0 and zero==n-1:
        print('0')
    else:
        string = s[:one]+s[zero:]
        print(string)
