n=int(input('Enter number of edges: '))

l=[]
for i in range(n):
    a,b=map(int,input('Enter source to destination: ').split())
    l.append((a,b))
    l.append((b,a))
    
