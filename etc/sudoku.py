board = [[int(x) for x in input().split()] for i in range(9)]
zeros =[]
for i,first in enumerate(board):
    for j,second in enumerate(first):
        if second==0:
            zeros.append((i,j))

def box(y,x,num):
    sx = x//3 * 3
    sy = y//3 * 3

    for i in range(3):
        for j in range(3):
            if num==board[sy+i][sx+j]:
                return False

    return True

def sudoku(n):
    if n == len(zeros):
        for a in board:
            print(*a)
        return True
    y =zeros[n][0]
    x =zeros[n][1]

    sx = x // 3 * 3
    sy = y // 3 * 3

    for i in range(1,10):
        flag =0
        for j in range(9):
            if i == board[y][j]:
                flag=1
                break
            if i == board[j][x]:
                flag=1
                break

        for j in range(3):
            if flag:
                break
            for k in range(3):
                if i == board[sy + j][sx + k]:
                    flag = 1
                    break
        if not flag:
            board[y][x] = i
            if sudoku(n+1):
                return True
            board[y][x] = 0


sudoku(0)