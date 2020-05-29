for I in range(int(input())):
    row,col = map(int,input().split())

    result=0
    if col%2==1:
        result+=row//2
        if row%2==1:
            result+=1

        result+=((col-1)//2)*row
    else:
        result+=(col//2)*row

    print(result)
