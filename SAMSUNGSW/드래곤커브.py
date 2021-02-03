import sys
input = sys.stdin.readline

# 우, 상 ,좌, 하
dy=[0,-1,0,1]
dx=[1,0,-1,0]

N = int(input())

curves=[]
for _ in range(N):
    x,y,d,g = map(int,input().split())
    curves.append([x,y,d,g])

board=[[0]*101 for _ in range(101)]

def go(cx,cy,d,g):
    stack=[d]
    board[cy][cx] = 1
    cy,cx = cy+dy[d],cx+dx[d]
    if cy >= 0 and cx >= 0 and cy < 101 and cx < 101:
        board[cy][cx]=1

    for gen in range(1,g+1):
        for i in range(len(stack)-1,-1,-1):
            curd = (stack[i]+1) % 4
            cy,cx = cy+dy[curd],cx+dx[curd]
            stack.append(curd)
            if cy>=0 and cx>=0 and cy<101 and cx<101:
                board[cy][cx]=1

for x,y,d,g in curves:
    go(x,y,d,g)

cnt=0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            cnt+=1

print(cnt)