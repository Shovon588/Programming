for _ in range(int(input())):
    s = input()
    l = len(s)

    one=-1;zero=-1
    for i in range(l):
        if s[i]=='0' and zero==-1:
            zero=i
        if s[i]=='1' and one==-1:
            one=i

    if one==-1:
        print('0'*(2*l))
    elif zero==-1:
        print('1'*(2*l))
    elif one<zero:
        print('10'*l)
    else:
        print('01'*l)
