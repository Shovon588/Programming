t = int(input())
for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))

        temp = list(set(a))
        if len(temp)>k:
                print(-1)
        else:
                for i in range(k-len(temp)):
                        temp.append(1)

                for i in range(n):
                        print(*temp, end=' ')
