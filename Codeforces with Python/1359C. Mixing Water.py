from math import ceil

for I in range(int(input())):
    h,c,t = map(int,input().split())

    low=0;high=1000006; totbest=1000006; move=1000006

    if (h+c)/2==t:
        print(2)
    else:
        while(low<high):
            best=1000006
            mid = ceil((low+high)/2)

            temp1 = abs(t-((h+c)*mid)/(2*mid))
            temp2 = abs(t-(((h+c)*mid)-c)/((2*mid)-1))
            temp3 = abs(t-(((h+c)*mid)+h)/((2*mid)+1))

            temp = [(temp1,2*mid),(temp2,(2*mid)-1),(temp3,(2*mid+1))]
            temp.sort()

            if temp[0][0]<totbest:
                totbest=temp[0][0]
                move=temp[0][1]
            if temp[0][0]==totbest:
                if temp[0][1]<move:
                    move=temp[0][1]

            if totbest+t==t:
                break
            elif totbest+t>t:
                high=mid-1
            elif totbest+t<t:
                low=mid+1
            print(*temp)
        print(move)
