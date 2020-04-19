for _ in range(int(input())):
    s=input()
    t=input()

    temps=''.join(set(s))
    tempt=''.join(set(t))

    flag='notok'
    for i in temps:
        if i in tempt:
            flag='ok'
            break
    if flag=='ok':
        print('YES')
    else:
        print('NO')
