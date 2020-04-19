n = int(input())

a = input()
b = input()

c = a.count('0')

zero_one=0;one_one=0;zero_zero=0;
for i in range(n):
    if a[i]=='0' and b[i]=='0':
        zero_zero+=1
    elif a[i]=='1' and b[i]=='0':
        zero_one+=1
    elif a[i]=='1' and b[i]=='1':
        one_one+=1

print((c*zero_one)+(zero_zero*one_one))
