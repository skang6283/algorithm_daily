from collections import deque
import sys

dx = [0,0,-1,1]
dy = [-1,1,0,0]
row,col = map(int, sys.stdin.readline().split())
wall = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(row)]
visited = [[[0]*2 for _ in range(col)] for _ in range(row)]
visited[0][0][0]==1

def bfs():
    q = deque()
    q.append((0,0,0,0))

    while q:
        y,x,b,d = q.popleft()
        if y == row-1 and x == col-1:
            return d+1

        for i in range(4):
            ny, nx = y+dy[i],x+dx[i]
            if ny <0 or nx<0 or ny>=row or nx >=col: continue

            if wall[ny][nx] == 0 and visited[ny][nx][b] == 0:
                q.append((ny,nx,b,d+1))
                visited[ny][nx][b] = 1

            if wall[ny][nx] == 1 and b == 0:
                q.append((ny,nx,1,d+1))
                visited[ny][nx][b] =1

    return -1

print(bfs())