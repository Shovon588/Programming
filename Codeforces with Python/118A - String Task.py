
n=input()
n=n.lower()

b=int (len(n))

vowels=['a','e','i','o','u','y']

for i in range (b):
    if n[i] in vowels:
        continue
    else:
        print ('.'+n[i], end='')
