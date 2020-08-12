def count_even(r,g,b,w):
    count = 0
    if r%2==0:count+=1
    if g%2==0:count+=1
    if b%2==0:count+=1
    if w%2==0:count+=1

    return count

for I in range(int(input())):
    r,g,b,w = map(int,input().split())

    if count_even(r,g,b,w)>2:
        print("Yes")
    else:
        if r>0 and g>0 and b>0:
            r-=1;g-=1;b-=1;w+=3

        if count_even(r,g,b,w)>2:
            print("Yes")
        else:
            print("No")

    
