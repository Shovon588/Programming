n = int(input())
ra, sa, pa = map(int,input().split())
rb, sb, pb = map(int,input().split())

maxi = 0
maxi += min(ra, sb)
maxi += min(pa, rb)
maxi += min(sa, pb)


mini = 0

sa = sa-rb
if sa>0:
    mini += max(0,sa-sb)

ra = ra-pb
if ra>0:
    mini += max(0, ra-rb)

pa = pa-sb
if pa>0:
    mini += max(0,pa-pb)

print(mini,maxi)

