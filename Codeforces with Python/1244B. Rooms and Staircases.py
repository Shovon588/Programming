for _ in range(int(input())):
    n=int(input())
    s=input()
    t=s[::-1]

    try:
        temps=s.index('1')+1
        tempt=t.index('1')+1
        temps=(n-temps)+1
        tempt=(n-tempt)+1

        res=max(temps,tempt)
        res=res*2
    except ValueError:
        res=n

    print(res)
