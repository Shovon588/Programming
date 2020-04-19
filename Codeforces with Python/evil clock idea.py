import datetime
import time

while(1):
    a=datetime.datetime.now()
    hour=a.hour
    minute=a.second

    print('')

    a = [0]*10
    b = [0]*40

    if hour%2!=0:
        a[1]=1
        hour-=1

    if hour>=8:
        a[8]=1
        hour-=8

    if hour>=4:
        a[4]=1
        hour-=4

    if hour>=2:
        a[2]=1
        hour-=2

    if minute%2!=0:
        b[1]=1

    if minute>=32:
        b[32]=1
        minute-=32

    if minute>=16:
        b[16]=1
        minute-=16

    if minute>=8:
        b[8]=1
        minute-=8

    if minute>=4:
        b[4]=1
        minute-=4

    if minute>=2:
        b[2]=1
        minute-=2

    print('Hour =',end=' ')
    for i in range(10):
        if a[i]==1:
            print (i,end=' ')

    print('Minute =',end=' ')
    for i in range(40):
        if b[i]==1:
            print (i,end=' ')

