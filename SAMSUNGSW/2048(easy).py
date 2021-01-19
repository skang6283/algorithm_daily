import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ans,q = 0,deque()

#push up down left right
dy=[1,-1,0,0]
dx=[0,0,1,-1]

def merge(d,sy,sx):
    px=dx[d]
    py=dy[d]
    while q:
        cur = q.popleft()

        if not board[sy][sx]:
            board[sy][sx]= cur
        elif board[sy][sx] == cur:
            board[sy][sx] +=cur
            sy+=py; sx+=px
        elif board[sy][sx] != cur:
            sy+=py; sx+=px
            board[sy][sx] = cur


def move(d):
    if d == 0: # push up
        for i in range(N):
            for j in range(N):
                if board[j][i]:
                    q.append(board[j][i])
                    board[j][i]=0
            merge(d,0,i)

    if d == 1: # push down
        for i in range(N):
            for j in range(N-1,-1,-1):
                if board[j][i]:
                    q.append(board[j][i])
                    board[j][i]=0

            merge(d, N-1, i)

    if d == 2: # push left
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    q.append(board[i][j])
                    board[i][j]=0

            merge(d, i, 0)

    if d == 3:  # push right
        for i in range(N):
            for j in range(N-1,-1,-1):
                if board[i][j]:
                    q.append(board[i][j])
                    board[i][j]=0

            merge(d, i, N-1)


def dfs(cnt):
    global board,ans
    if cnt >=5:
        ans = max(max([max(b) for b in board]),ans)
        return

    temp =[x[:] for x in board]
    for i in range(4):
        move(i)
        dfs(cnt+1)
        board=[x[:] for x in temp]


dfs(0)
print(ans)