def lps(seq, i, j): 
	 
    if (i == j): 
        return 1

    if (seq[i] == seq[j] and i + 1 == j): 
        return 2

    if (seq[i] == seq[j]):
        return lps(seq, i + 1, j - 1) + 2

    return max(lps(seq, i, j - 1), 
                    lps(seq, i + 1, j)) 

def lps2(seq, i, j): 
	 
    if (i == j): 
        return (1,1)

    if (seq[i] == seq[j] and i + 1 == j): 
        return (2,1)

    if (seq[i] == seq[j]):
        return (lps2(seq, i + 1, j - 1) + 2,2)
    

    len1, u1 = lps2(seq, i, j - 1)
    len2, u2 = lps2(seq, i + 1, j)

    if u1<=2 and u2<=2:
        return max(len1,len2)
    elif u1>=3:
        return len2
    elif u2>=3:
        return len1
    

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    res = lps(a,0,n-1)

    print(res)
