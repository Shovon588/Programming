dic = {2: 1, 3: 7, 4:4, 5: 5, 6: 9, 7: 8}

for i in range(int(input())):
    n = int(input())
    string = ''

    if n%2==0:
        temp = n//2
        print('1'*temp)
    else:
        temp = n-3
        string+='7'
        temp = temp//2
        string+='1'*temp
        print(string)
