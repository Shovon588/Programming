def transform(a,b):
    a = list(a)
    b = list(b)
    lista = [int(num) for num in a]
    listb = [int(num) for num in b]
    a = sum(lista)
    b = sum(listb)

    return a,b

for I in range(int(input())):
    n = int(input())
    chef = 0
    morty = 0
    for i in range(n):
        a,b = map(str,input().split())
        a,b = transform(a,b)
        if a>b:
            chef+=1
        elif b>a:
            morty+=1
        else:
            chef+=1
            morty+=1
            
    if chef>morty:
        print(0,chef)
    elif morty>chef:
        print(1,morty)
    else:
        print(2,chef)
