for I in range(int(input())):
    n = int(input())

    mat = []
    for i in range(n):
        s = list(input())
        mat.append(s)

    result='YES'
    for i in range(n):
        for j in range(n):
            if mat[i][j]=='1':
                if i!=n-1 and j!=n-1:
                    if mat[i][j+1]=='0' and mat[i+1][j]=='0':
                        result='NO'
    print(result)

