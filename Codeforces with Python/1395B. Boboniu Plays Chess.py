n,m,x,y = map(int,input().split())

arr = [[-1 for i in range(m)] for i in range(n)]

arr[x-1][y-1]=1
print(x,y)


while(1):
    if y-1>=1:
        y-=1
    else:
        break

    if arr[x-1][y-1]==-1:
        arr[x-1][y-1]=1
        print(x,y)

while(1):
    if y+1<=m:
        y+=1
    else:
        break

    if arr[x-1][y-1]==-1:
        arr[x-1][y-1]=1
        print(x,y)


x = 1
if arr[x-1][y-1]==-1:
    arr[x-1][y-1]=1
    print(x,y)


next_move = 'left'
while(1):
    if next_move=='right':
        if y+1<=m:
            y+=1
        else:
            next_move='left'
            while x<=n:
                if arr[x-1][y-1]==-1:
                    print(x)
                    break
                x+=1
    else:
        if y-1>=1:
            y-=1
        else:
            next_move='right'
            while x<=n:
                if arr[x-1][y-1]==-1:
                    break
                x+=1

    if x>n:
        break

    if arr[x-1][y-1]==-1:
        arr[x-1][y-1]=1
        print(x,y)
    else:
        pass

