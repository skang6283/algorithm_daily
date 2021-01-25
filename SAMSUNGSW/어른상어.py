import sys

input = sys.stdin.readline
dy=[-1,1,0,0]
dx=[0,0,-1,1]
# 상 하 좌 우
# 0 1 2 3

N,M,K = map(int,input().split())
scent_board = [list(map(int,input().split())) for _ in range(N)]
shark_dir = list(map(int,input().split()))
shark_dir = [w-1 for w in shark_dir]
shark_loc =[[] for _ in range(M)]
shark_board=[[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if scent_board[i][j] != 0:
            shark_loc[scent_board[i][j]-1]=[i,j]
            tmp = scent_board[i][j]
            shark_board[i][j].append(scent_board[i][j]-1)
            scent_board[i][j] = [tmp-1, K]
        else:
            scent_board[i][j] = [-1,0]   # sharkNum, Scent

dir_info = [[list(map(int,input().split())) for _ in range(4)] for _ in range(M)]
dir_info = [[[d -1 for d in dir]for dir in shark]for shark in dir_info]
cnt =M

def move(cnt):
    for cur in range(M):

        cd = shark_dir[cur]
        if cd == -1:continue
        cy,cx = shark_loc[cur]

        for i in range(4):
            nd = dir_info[cur][cd][i]
            ny,nx = cy+dy[nd] , cx+ dx[nd]
            if ny>=0 and nx>=0 and ny<N and nx<N:
                if scent_board[ny][nx][0] == -1:
                    shark_dir[cur] = nd
                    shark_board[ny][nx].append(cur)
                    shark_board[cy][cx].pop(0)
                    shark_loc[cur]=[ny,nx]
                    break
        else:
            for i in range(4):
                nd = dir_info[cur][cd][i]
                ny, nx = cy + dy[dir_info[cur][cd][i]], cx + dx[dir_info[cur][cd][i]]
                if ny >= 0 and nx >= 0 and ny < N and nx< N:
                    if scent_board[ny][nx][0] == cur:
                        shark_dir[cur] = nd
                        shark_board[ny][nx].append(cur)
                        shark_board[cy][cx].pop(0)
                        shark_loc[cur] = [ny, nx]
                        break

    dead = []
    for i in range(N):
        for j in range(N):
            if scent_board[i][j][1]:
                scent_board[i][j][1] -=1
            if scent_board[i][j][1] == 0:
                scent_board[i][j][0] =-1

            if len(shark_board[i][j]) >=2:
                dead.extend(shark_board[i][j][1:])
                shark_board[i][j] = shark_board[i][j][:1]

            if shark_board[i][j]:
                scent_board[i][j]=[shark_board[i][j][0],K]

    for shark in dead:
        shark_dir[shark]= -1
        cnt -= 1
    return cnt

if M <=1:
    print(0)
    sys.exit()
for ans in range(1000):
    cnt =move(cnt)
    if cnt == 1:
        print(ans+1)
        sys.exit()
print(-1)