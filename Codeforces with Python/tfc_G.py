w,h,x,y,r = map(int,input().split())

if x+r>w or y+r>h or x<0 or y<0:
    print('No')
else:
    print("Yes")
        
