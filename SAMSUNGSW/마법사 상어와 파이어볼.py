import sys,math
input = sys.stdin.readline

dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,1,1,1,0,-1,-1,-1]


N,M,K = map(int,input().split())

index = 0
present_fireballs =0

board = [[[]for _ in range(N)]for _ in range(N)]
for index in range(M):
    r, c, m, s, d = map(int,input().split())
    board[r-1][c-1].append([r-1,c-1,m,s,d])
    index+=1


def move():
    global board
    new_board = [[[]for _ in range(N)]for _ in range(N)]
    # print("original")
    # for a in board:
    #     print(a)
    # print()
    for i in range(N):
        for j in range(N):
            for fireball in board[i][j]:
                y,x,m,s,d = fireball
                ny,nx = (y+dy[d]*s)%N,(x+dx[d]*s)%N
                new_board[ny][nx].append([ny,nx,m,s,d])

    # print("moved")
    # for a in new_board:
    #     print(a)
    # print()

    m,s,d=2,3,4
    tmp_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not new_board[i][j]: continue

            if len(new_board[i][j]) == 1:
                tmp_board[i][j].append(new_board[i][j][0])
                continue

            nm,ns,nd= 0,0,0
            pre_d =-1
            for fireball in new_board[i][j]:
                nm+=fireball[m]
                ns+=fireball[s]
                if fireball[d] % 2 != pre_d and pre_d != -1:
                    nd = 1
                pre_d = fireball[d] % 2

            nm = math.floor(nm / 5)
            ns = math.floor(ns/len(new_board[i][j]))

            if nm <=0: continue
            if not nd: # 0,2,4,6
                for dir in [0,2,4,6]:
                    tmp_board[i][j].append([i,j,nm,ns,dir])
            else:
                for dir in [1,3,5,7]:
                    tmp_board[i][j].append([i,j,nm,ns,dir])
    # print("split")
    # for a in board:
    #     print(a)
    # print()
    board = tmp_board

def calc():
    totalm=0
    for i in range(N):
        for j in range(N):
            for y,x,m,s,d in board[i][j]:
                totalm+=m
    return totalm

for _ in range(K):
    move()
    #print(calc())


#print("###")
print(calc())
