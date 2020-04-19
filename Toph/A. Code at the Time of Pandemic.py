for z in range(int(input())):
    n = int(input())

    new=0; total=1

    print("Case %d:" %(z+1))
    for i in range(n):
        print("Day = %d, New = %d, Total = %d" %(i+1,new,total))
        new = 2*total
        total+=new
        
