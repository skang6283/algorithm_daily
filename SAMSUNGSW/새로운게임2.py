import sys

input = sys.stdin.readline
N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]  #
chessPieces = []
pos=[[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    r,c,d = map(int,input().split())
    chessPieces.append([r-1,c-1,d-1])
    pos[r-1][c-1].append(i)

dy,dx= [0,0,-1,1], [1,-1,0,0] #우,좌,상,하

def move(piece_num): # white:0   red:1   blue:2
    y,x,dir = chessPieces[piece_num]
    ny,nx = y+dy[dir], x+dx[dir]

    if ny<0 or nx<0 or ny>=N or nx>=N or board[ny][nx] == 2:        # 파랑,벽 체크
        if dir == 0 or dir ==2:
            dir +=1
        else:
            dir -=1
        chessPieces[piece_num][2] = dir
        ny,nx = y+dy[dir], x+dx[dir]

    if ny < 0 or nx < 0 or ny >= N or nx >= N or board[ny][nx] == 2: # 다시 한번 체
        return 0

    stack,tmp=[],-1                                 # 위에있는거 가져고기 pop이라 이미 reversed 되있
    while tmp != piece_num:
        tmp = pos[y][x].pop()
        stack.append(tmp)


    if board[ny][nx] == 0:                        # 하 reverse 후 extend
        stack.reverse()

    pos[ny][nx].extend(stack)
    for i in stack:                                 # 체스피스 위치 업뎃
        chessPieces[i][0], chessPieces[i][1] = ny, nx

    stack = []
    for i, key in enumerate(pos[y][x]):
        if key == piece_num:
            stack.extend(pos[y][x][i:])
            pos[x][y] = pos[y][x][:i]
            break

    if board[ny][nx] == 1:
        stack = stack[-1::-1]

    for i in stack:
        pos[ny][nx].append(i)
        chessPieces[i][:2] = [ny, nx]


    if len(pos[ny][nx]) >= 4:                       # 스택이 4 이상 쌓였으면 리턴 1
        return 1
    return 0

cnt=1
while cnt <= 1000:
    for i in range(K):
        if move(i) == 1:
            print(cnt)
            sys.exit()
    cnt+=1

print(-1)



