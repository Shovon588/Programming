w1,h1,w2,h2=map(int,input().split())

left=h1+h2
down=w1
corner=4

if w1==w2:
     up=w1
     right=h1+h2
else:
     up=w2
     right=h1+h2+abs((w2+1)-(w1+1))

print(left+right+up+down+corner)
