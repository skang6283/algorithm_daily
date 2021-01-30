import sys,math

input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

#좌 하 우 상
#0 1 2 3

dy=[ [-1,-1,-1,-2, 0, 1, 1, 1, 2],  # 좌
     [-1, 0, 1, 0, 2,-1, 0, 1, 0],   # 하
     [ 1, 1, 1, 2, 0,-1,-1,-1,-2],   # 우
     [ 1, 0,-1, 0,-2, 1, 0,-1, 0] ]  # 상

dx=[ [ 1, 0,-1, 0,-2, 1, 0,-1, 0], #좌
     [-1,-1,-1,-2, 0, 1, 1, 1, 2], #하
     [-1, 0, 1, 0, 2,-1, 0, 1, 0], #우
     [ 1, 1, 1, 2, 0,-1,-1,-1,-2] ] #상


percent =[1,7,10,2,5,1,7,10,2]
ny=[0,1,0,-1]
nx=[-1,0,1,0]

def spread(yy,yx,dir):
    out,moved =0,0
    original = board[yy][yx]
    board[yy][yx] =0
    for index in range(len(percent)):
        dust = math.floor(original * percent[index]/100)
        dusty, dustx = yy+dy[dir][index], yx+dx[dir][index]

        if dusty<0 or dustx<0 or dusty>=N or dustx>=N:
            out += dust
        else:
            board[dusty][dustx] += dust
        moved += dust
    ay,ax = yy+ny[dir],yx+nx[dir]

    if ay < 0 or ax < 0 or ay >= N or ax >= N:
        out += original - moved
    else:
        board[ay][ax] += original - moved

    return out

def go():
    ans=0
    dist = 0
    dir = 0
    yy,yx = N//2,N//2
    move=2
    while not(yy==0 and yx==0):
        dist += 1
        if dist == (N-1): move=3
        for i in range(move):
            for _ in range(dist):
                yy, yx = yy + ny[dir], yx + nx[dir]
                ans += spread(yy,yx,dir)
            dir = (dir+1)%4
    return ans

print(go())