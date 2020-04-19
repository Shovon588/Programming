t = int(input())

for z in range(t):
    n = int(input())
    
    lastp=0; lastc=0
    flag='YES'
    for i in range(n):
        play, clear = map(int,input().split())

        if clear>play:
            flag='NO'

        if play<lastp or clear<lastc:
            flag='NO'

        if abs(lastc-clear)>abs(lastp-play):
            flag='NO'

        lastp=play; lastc=clear

    print(flag)
