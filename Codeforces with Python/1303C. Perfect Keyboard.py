adjacent = {}

for _ in range(int(input())):
    s=input()

    unique = ''.join(set(s))

    for i in range(1,len(s)-1):
        left=s[i-1]
        right=s[i+1]
        mid=s[i]

        try:
            if adjacent[mid]:
                if left not in adjacent[mid]:
                    adjacent[mid].append(left)
                if right not in adjacent[mid]:
                    adjacent[mid].append(right)
        except KeyError:
            adjacent[mid] = [left]
            if right not in adjacent[mid]:
                adjacent[mid].append(right)

    res = ''

    for temp in adjacent:
        if len(adjacent[temp])>2:
            print('hobe na')
            break
        else:
            if len(res)==0:
                if len(adjacent[temp])==2:
                    res+=adjacent[temp][0]+temp+adjacent[temp][1]
                else:
                    res+=adjacent[temp][0]+temp

            else:
                if temp in res:
                    if res[0]==temp or res[-1]==temp:
                        
            
            
