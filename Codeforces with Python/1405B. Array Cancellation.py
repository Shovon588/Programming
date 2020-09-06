for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    negsum = 0

    for num in a:
        if num<0:
            negsum+=num

    operation = []
    carry = 0
    for i in range(n):
        if a[i]>0:
            operation.append((a[i],abs(negsum)))
            negsum=min(0,negsum+a[i])
            carry+=a[i]
        else:
            if abs(a[i])>=carry:
                negsum+=abs(abs(a[i])-carry)
                carry=0
            else:
                carry+=a[i]
                

    result = 0
    for i in range(len(operation)):
        if operation[i][0]>operation[i][1]:
            result += operation[i][0]-operation[i][1]
    print(result)
