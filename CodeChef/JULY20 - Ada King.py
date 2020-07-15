for I in range(int(input())):
    n = int(input())

    col = n//8
    row = n%8

    if col==0:
        print('O',end='')
        for i in range(row-1):
            print('.',end='')
        for i in range(8-row):
            print('X',end='')
        print()
        for i in range(7):
            print('XXXXXXXX')
    else:
        print('O.......')
        
        for i in range(col-1):
            print('........')

        if row>0:
            for i in range(row):
                print('.',end='')
            for i in range(8-row):
                print('X',end='')
            print()
            for i in range(8-col-1):
                print('XXXXXXXX')
        else:
            for i in range(8-col):
                print('XXXXXXXX')
    print()


