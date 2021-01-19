import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N,M = map(int, input().split())
lab = [list(map(int,input().split())) for _ in range(N)]


viruses=[]

dy=[-1,1,0,0]
dx=[0,0,-1,1]

minv=sys.maxsize
zeros=0
empty=[]
for y in range(N):
    for x in range(M):
        if lab[y][x] == 2:
            viruses.append((y,x))
        if lab[y][x] == 0:
            zeros+=1
            empty.append((y,x))


def spread():
    v=deque(viruses)
    temp = [x[:] for x in lab]
    vcnt = 0

    while v:
        cury,curx = v.popleft()
        for i in range(4):
            ny,nx = cury+dy[i],curx+dx[i]
            if ny<0 or nx<0 or ny>=N or nx>=M: continue

            if temp[ny][nx] == 0:
                vcnt+=1
                if vcnt>=minv:
                    return minv

                temp[ny][nx]=2
                v.append((ny,nx))
    return vcnt

def solve():
    global minv,lab


    for spots in combinations(empty,3):
        for y,x in spots:
            lab[y][x]=1
        minv = min(spread(),minv)

        for y, x in spots:
            lab[y][x] = 0


solve()
print(zeros-minv-3)
