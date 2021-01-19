import sys
from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

col,row = map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(row)]
q = deque()
tempq = deque()


for y in range(row):
    for x in range(col):
        if tomato[y][x] == 1:
            q.append((y,x))

def bfs():
    day=0
    while q:

        while q:
            tempq.append(q.popleft())

        while tempq:
            y,x = tempq.popleft()
            for i in range(4):
                ny,nx = y+dy[i],x+dx[i]
                if ny <0 or nx <0 or ny >= row or nx>=col: continue
                if tomato[ny][nx] == 0:
                    q.append((ny,nx))
                    tomato[ny][nx]=1
        day += 1

    return day-1

day=0
if q:
    day=bfs()
    for t in tomato:
        for a in t:
            if a == 0:
                day = -1

print(day)