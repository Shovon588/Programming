from sys import stdin,stdout
a=stdin.readline()
list=[]
while(a):
    list.append(a[:2])
    a=a[2:]
