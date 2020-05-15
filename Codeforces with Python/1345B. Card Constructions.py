cards = []

for i in range(1,30000):
    piramid = (i*(i+1))//2
    stick = (i*(i-1))//2
    temp = (piramid*2)+stick
    cards.append(temp)

    if temp>1000000009:
        break

def solve(n):
    left = 0; right = 25819
    while(right-left>1):
        mid = (left+right)//2
        print(left,right,mid)

        if n==cards[mid]:
            print('okay')
            break
        if n>cards[left] and n<cards[mid]:
            print('ya')
            right = mid-1
        elif n>cards[mid] and n<cards[right]:
            print('hmm')
            left=mid+1


solve(1)
            
            
