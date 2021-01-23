import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
blocks=[list(map(int,input().split())) for _ in range(N)] # t, x, y,
# t=1 1x1,   t=2 (x,y)(x,y+1),    t=3 (x,y)(x+1,y)


green=deque([[0,0,0,0] for _ in range(6)])
blue=deque([[0,0,0,0] for _ in range(6)])
score=0

def pb():
    for i in range(3,-1,-1):
        for j in range(6):
            print(blue[j][i], end=" ")
        print()
    print()

def pg():
    for a in green:
        print(a)
    print()


def move(type,board,t,x,y):
    x=0
    if t == 1:
        while x<6 and board[x][y] == 0 :
            x+=1
        board[x-1][y]=1

    elif t == 2:
        if type =='g':  #green
            while x < 6 and board[x][y] == 0 and board[x][y + 1] == 0:
                x+=1
            board[x - 1][y] = 1
            board[x - 1][y + 1] = 1
        else:           #blue
            while x < 5 and board[x][y] == 0 and board[x+1][y] == 0:
                x+=1
            board[x-1][y] = 1
            board[x][y] = 1

    elif t == 3:
        if type =='g':  #green
            while x < 5 and board[x][y] == 0 and board[x+1][y] == 0 :
                x+=1
            board[x - 1][y] = 1
            board[x][y] = 1
        else:           #blue
            x+=1
            while x < 6 and board[x][y] == 0 and board[x][y-1] == 0:
                x+=1
            board[x-1][y-1] = 1
            board[x-1][y] = 1

def check(board):
    global score
    for i in range(2,6):
        if 0 not in board[i]:
            del board[i]
            board.appendleft([0,0,0,0])
            score+=1


    for i in range(0,2):
        if 1 in board[i]:
            board.pop()
            board.appendleft([0,0,0,0])

def solve(t,x,y):
    move('g',green,t,x,y)
    move("b",blue, t,y,3-x)
    check(green)
    check(blue)

def count():
    cnt=0
    for i in range(2,6):
        for j in range(4):
            cnt+=blue[i][j]
            cnt+=green[i][j]
    return cnt
for t,x,y in blocks:

    solve(t,x,y)
print(score)
print(count())

