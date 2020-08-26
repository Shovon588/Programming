T = int(input())
 
for _ in range(T):
    N = int(input())
    s = list(input())


    d = {"0": [], "1": []}
    move = 0
    ans = []
    for c in s:
        print(d)
        if c == "1":
            arr = d["0"]
            if not len(arr) == 0:
                    tmp = arr.pop()
                    ans.append(tmp)
                    d["1"].append(tmp)
            else:
                    move += 1
                    ans.append(move)
                    d["1"].append(move)
        else:
            arr = d["1"]
            if not len(arr) == 0:
                    tmp = arr.pop()
                    ans.append(tmp)
                    d["0"].append(tmp)
            else:
                    move += 1
                    ans.append(move)
                    d["0"].append(move)

    print(move)
    print(*ans)
