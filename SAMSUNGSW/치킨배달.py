import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(N)]

home=[]
chicken=[]
dy=[-1,1,0,0]
dx=[0,0,-1,1]


for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            home.append((i,j))
        if city[i][j]==2:
            chicken.append((i,j))

ans=sys.maxsize

def getmin(y,x,curc):
    mind = sys.maxsize
    for cy,cx in curc:
        mind = min(mind,abs(cy-y)+abs(cx-x))

    return mind

for comb in list(combinations(chicken,M)):
    tmp=0

    for hy,hx in home:
        tmp+= getmin(hy,hx,comb)

    ans = min(ans,tmp)

print(ans)







