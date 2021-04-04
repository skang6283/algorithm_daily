import sys
from collections import deque

d = [
    [(0,1,0,1),(0,1,1,1)],              # 0 horizontal
    [(1,0,1,0),(1,0,1,1)],              # 1 vertical
    [(1,1,0,1),(1,1,1,0),(1,1,1,1)]     # 2 diagonal
     ]  # 2 diagonal


input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def checkdir(y1,x1,y2,x2):
    if y1 == y2: return 0       # horizontal
    elif x1 == x2: return 1     # vertical
    return 2                    # diagonal

def bfs():
    q = deque()
    q.append((0,0,0,1))
    cnt = 0

    while q:
        y1,x1,y2,x2 = q.popleft()

        for py1,px1,py2,px2 in d[checkdir(y1,x1,y2,x2)]:
            ny1=y1+py1; nx1=x1+px1
            ny2=y2+py2; nx2=x2+px2

            if ny2>=N or nx2>=N or board[ny2][nx2]==1: continue
            if py2==1 and px2==1:
                if board[ny2-1][nx2]==1 or board[ny2][nx2-1]==1: continue

            if ny2 ==(N-1) and nx2 ==(N-1):
                cnt += 1
                break
            q.append((ny1,nx1,ny2,nx2))

    return cnt

def dfs():


print(bfs())
