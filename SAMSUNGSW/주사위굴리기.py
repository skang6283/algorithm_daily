import sys
from collections import deque
input = sys.stdin.readline

#   2
# 4 1 3
#   5
#   6
N,M,y,x,K = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
cmd = list(map(int,input().split()))

dice =[0,0,0,0,0,0,0]

vert = deque([2,1,5,6])
hor = deque([4,1,3])

# 우 좌 상 하

dy=[0,0,-1,1]
dx=[1,-1,0,0]
def move(dir):
    if dir == 2:
        hor[1] = vert[0]
        vert.appendleft(vert.pop())
    elif dir == 3:
        hor[1] = vert[2]
        vert.append(vert.popleft())
    elif dir == 0:
        vert[1] = hor[2]
        hor.append(vert.pop())
        vert.append(hor.popleft())
    else:
        vert[1] = hor[0]
        hor.appendleft(vert.pop())
        vert.append(hor.pop())

def go(dir,y,x):
    move(dir)

    if board[y][x] ==0:
        board[y][x] = dice[vert[1]]
    else:
        dice[vert[1]] = board[y][x]
        board[y][x]=0

    print(dice[vert[3]])

for d in cmd:

    d-=1
    ny, nx = y + dy[d], x + dx[d]
    if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
    y,x=ny,nx
    go(d,y,x)


