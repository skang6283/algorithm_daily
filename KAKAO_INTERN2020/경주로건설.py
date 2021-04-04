import sys
from heapq import *
# 0,1,2,3
# left, right, down, up
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    n=len(board)
    cost_board = [[[sys.maxsize]*n for _ in range(n)] for _ in range(4)]

    pq=[]
    pq.append((0,0,0,-1))
    cost_board[0][0][0] = 100
    cost_board[1][0][0] = 100
    cost_board[2][0][0] = 100
    cost_board[3][0][0] = 100

    while pq:
        price,cy,cx,dir = heappop(pq)
        if price > cost_board[dir][cy][cx]: continue

        for i in range(4):
            ny = cy + dy[i]; nx = cx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == 1: continue

            if dir == -1 or (dir == i):
                p = 100
            else:
                p = 600


            oldp = cost_board[i][ny][nx]
            newp = p+price

            if newp < oldp:
                heappush(pq,(newp,ny,nx,i))
                if dir==-1: continue
                cost_board[i][ny][nx]=newp

        for a in cost_board:
            for row in a:
                print(row)
            print()
        print()

    return min(cost_board[0][n-1][n-1],cost_board[1][n-1][n-1],cost_board[2][n-1][n-1],cost_board[3][n-1][n-1])

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))