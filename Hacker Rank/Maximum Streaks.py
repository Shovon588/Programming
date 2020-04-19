n = int(input())
toss = []

for i in range(n):
    s = input()
    toss.append(s)

head = 0; tail = 0
curr = toss[0]
streak = 1
for i in range(1,n):
    result = toss[i]
    if result==curr:
        streak+=1
    else:
        if curr=='Heads':
            head=max(head,streak)
        else:
            tail=max(tail,streak)

        curr=result
        streak=1
if curr=='Heads':
    head=max(head,streak)
else:
    tail=max(tail,streak)

arr = [head,tail]
    
