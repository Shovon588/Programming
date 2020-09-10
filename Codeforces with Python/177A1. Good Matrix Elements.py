n = int(input())

matrix = []
for i in range(n):
    a = list(map(int,input().split()))

    matrix.append(a)


visited = {}
result = 0
for i in range(n):
    for j in range(n):
        if i==j and ((i,j) not in visited):
            result+=matrix[i][j]
            visited[(i,j)]=True

        if (i+j)==n-1 and ((i,j) not in visited):
            result+=matrix[i][j]
            visited[(i,j)]=True

        if i==n//2 and ((i,j) not in visited):
            result+=matrix[i][j]
            visited[(i,j)]=True

        if j==n//2 and ((i,j) not in visited):
            result+=matrix[i][j]
            visited[(i,j)]=True

print(result)
                
                
        
