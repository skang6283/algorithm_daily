import sys
from collections import deque

input = sys.stdin.readline
row,col = map(int,input().split())
board = [list(input().strip()) for _ in range(row)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

srx,sry,sbx,sby,desty,destx =0,0,0,0,0,0
for y in range(row):
    for x in range(col):
        if board[y][x] =='R':
            sry, srx = y,x
            board[y][x] ='.'
        elif board[y][x] == 'B':
            sby,sbx = y,x
            board[y][x] ='.'
        elif board[y][x] =='O':
            desty,destx = y,x
            board[y][x] ='.'

def move(y, x, dy, dx):
    goal = 0
    dist_traveled=0
    while board[y][x] == '.':
        y += dy
        x += dx
        if y == desty and x == destx:
            goal = 1
        dist_traveled+=1
    y -= dy
    x -= dx

    return y, x, goal,dist_traveled

def solve(ry,rx,by,bx):
    visited = set()
    q = deque()
    q.append((ry,rx,by,bx,0))
    visited.add((ry,rx,by,bx))
    cnt=0
    while q:
        cry,crx,cby,cbx,cnt = q.popleft()


        if cnt >= 10:
            continue

        for i in range(4):
            nry, nrx,success,rd = move(cry,crx,dy[i],dx[i])
            nby, nbx,fail,bd = move(cby,cbx,dy[i],dx[i])

            if nry == nby and nrx == nbx:
                if rd > bd:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -=dy[i]
                    nbx -=dx[i]

            if not fail and success:
                return cnt+1

            if not fail and (nry,nrx,nby,nbx) not in visited:
                q.append((nry,nrx,nby,nbx,cnt+1))
                visited.add((nry,nrx,nby,nbx))



    return -1

ans = solve(sry,srx,sby,sbx)
print(ans)
