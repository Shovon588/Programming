for i in range(int(input())):
    s=input()

    left = s.count('L')
    right = s.count('R')
    up = s.count('U')
    down = s.count('D')

    left=min(left,right)
    right=left
    up=min(up,down)
    down=up

    if left==0 and up==0:
        pass
    elif up==0:
        left=1;right=1
    elif left==0:
        up=1;down=1

    print(left+right+up+down)
    print(('L'*left)+('U'*up)+('R'*right)+('D'*down))


