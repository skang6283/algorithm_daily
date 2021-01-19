import sys
from collections import deque
from heapq import *

input =sys.stdin.readline
dy=[-1,0,0,1]
dx=[0,-1,1,0]

N = int(input())
tank=[list(map(int,input().split())) for _ in range(N)]

size=2
cnt=0
by,bx=0,0

for i in range(N):
    for j in range(N):
        if tank[i][j] == 9:
            by,bx =i,j
            tank[by][bx]=0
def bfs():
    global by,bx
    q = deque()
    h=[]

    mind=sys.maxsize
    q.append((by,bx,0))
    visited=[[False]*N for _ in range(N)]
    visited[by][bx]=True

    while q:
        cy,cx,cd = q.popleft()


        for i in range(4):
            ny,nx = cy+dy[i],cx+dx[i]
            if ny <0 or nx<0 or ny>=N or nx>=N: continue
            if visited[ny][nx]: continue

            if tank[ny][nx] ==0 or tank[ny][nx] == size:
                q.append((ny,nx,cd+1))
                visited[ny][nx]=True
                continue
            if tank[ny][nx] < size and cd<=mind:
                heappush(h,(cd+1,ny,nx))
                mind = min(mind,cd)


    if len(h) == 0:
        return 0
    d,y,x = heappop(h)
    by, bx = y,x

    tank[y][x]=0
    return d

cnt=0
total_dist=0
while True:
    dist = bfs()
    if dist:
        total_dist+=dist
        cnt+=1
        if cnt==size:
            cnt=0
            size+=1
    else:
        break


print(total_dist)
