cnt = 0
board = []


def dia(y, x,py,px,n):

    cy, cx = y, x
    while cy>=0 and cx>=0 and cy<n and cx<n:
        if board[cy][cx]:
            return False
        cy += py
        cx += px
    return True

def vert(y,x,n):
    cy = 0
    while cy < n:
        if cy != y and board[cy][x]:
            return False
        cy += 1
    return True


def dfs(y, n):
    global cnt
    if y == n:
        cnt += 1
        for a in board:
            print(a)
        return

    for x in range(n):
        if dia(y,x,-1,-1,n) and dia(y,x,-1,1,n) and dia(y,x,1,-1,n) and dia(y,x,1,1,n) and vert(y,x,n):
            board[y][x] = 1
            dfs(y + 1, n)
            board[y][x] = 0


def solution(n):
    for _ in range(n):
        board.append([0] * n)
    print(board)
    dfs(0, n)

    return cnt

solution(4)
print(cnt)