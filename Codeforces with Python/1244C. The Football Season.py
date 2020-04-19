n,p,w,d=map(int,input().split())

win=p//w;rem=p-(win*w)

flag='notok'
while(1):
    if rem%d==0:
        draw=rem//d
        flag='ok'
        break
    if win-1>=0:
        win-=1;rem+=w
    else:
        break

if flag=='ok' and win+draw<=n:
    print(win,draw,n-win-draw)
else:
    print(-1)
