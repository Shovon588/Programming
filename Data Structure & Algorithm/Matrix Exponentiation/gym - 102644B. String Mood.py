n = int(input())

m = 1000000007

def multiply(a,b):
    product = [[0,0],
               [0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                product[i][k] += (a[i][j] * b[j][k])%m
    return product


def expo_power(arr,n):
    result = [[1,0],
              [0,1]]
    
    while n>0:
        if n%2==1:
            result = multiply(result,arr)

        arr = multiply(arr,arr)
        n = n//2
        print(arr)
    return result

arr = [[19,7],
        [6,20]]

result = expo_power(arr,n)

print(result[0][0]%m)


