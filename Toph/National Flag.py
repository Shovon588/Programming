x, y = map(int,input().split())

target = 1.6666666666666667

left = 0; right = x-5

while(1):
    mid = (left+right)//2

    tempx = x-mid
    tempy = y-mid

    if tempx/tempy==target:
        print(tempx, tempy)
        break
    elif (tempx/tempy)<target:
        left = mid+1
    else:
        right=mid-1

    if left>right:
        print('Not Possible')
        break
