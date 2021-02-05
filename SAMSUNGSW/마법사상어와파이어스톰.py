import sys
from collections import deque

input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]


N,Q = map(int,input().split())
N = 2**N
board = [list(map(int,input().split())) for _ in range(N)]
L = list(map(int,input().split()))

visited = [[0] * N for _ in range(N)]


def debug():
    for a in board:
        print(a)
    print()

def rotate(r,c,l):
    tmp = [[0]*l for _ in range(l)]

    for i in range(l):
        for j in range(l):
            tmp[i][j] = board[r+i][c+j]

    tmp = list(zip(*tmp[::-1]))

    for i in range(l):
        for j in range(l):
            board[r + i][c + j] = tmp[i][j]

def firestorm(l):

    # rotate
    if l >0:
        for i in range(0,N,l):
            for j in range(0,N,l):
                rotate(i,j,l)

    tmp=[]
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                cnt = 0
                for k in range(4):
                    ny,nx = y+dy[k],x+dx[k]
                    if ny<0 or nx<0 or ny>=N or nx>=N:continue
                    if board[ny][nx]:
                        cnt+=1
                if cnt < 3:
                    tmp.append([y,x])

    for y,x in tmp:
        board[y][x] -=1

def bfs(y,x):
    q = deque()
    q.append([y,x])
    size = 0

    while q:
        y,x = q.pop()
        for d in range(4):
            ny,nx = y+dy[d],x+dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue

            if board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.appendleft([ny,nx])
                size += 1
    return size

def find():
    total = 0
    most = 0
    for i in range(N):
        for j in range(N):
            total += board[i][j]

    for y in range(N):
        for x in range(N):
            if board[y][x] and not visited[y][x]:
                most = max(bfs(y,x),most)

    return total, most

for l in L:
    firestorm(2**l)

ans1,ans2 = find()
print(ans1)
print(ans2)