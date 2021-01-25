import sys
from copy import copy, deepcopy

input = sys.stdin.readline
dy = [-1, -1,  0,  1, 1, 1, 0, -1]
dx = [ 0, -1, -1, -1, 0, 1, 1,  1]
#0, 1, 2, 3, 4, 5, 6, 7,
#↑, ↖, ←, ↙, ↓, ↘, →, ↗

info= [list(map(int,input().split())) for _ in range(4)]
space=[[]*4 for _ in range(4)]
fish=[[] for _ in range(17)]
sy,sx,sd = 0,0,info[0][1]-1

for i in range(4):
    for j in range(0,8,2):
        a,b = info[i][j], info[i][j+1] # a:number , b:direction
        space[i].append(a)
        fish[a] = [i,j//2,b-1]

first = space[0][0]
space[0][0]=[]
fish[first] = []

most=0


def swap(ny,nx,y,x):

    if space[ny][nx]:
        fish[space[ny][nx]][0:2], fish[space[y][x]][0:2] = fish[space[y][x]][0:2], fish[space[ny][nx]][0:2]
    else:
        fish[space[y][x]][0:2] = [ny, nx]

    space[ny][nx],space[y][x]=space[y][x],space[ny][nx]


def dfs(cnt):
    global most
    global space,fish
    global sy,sx,sd
    most = max(most,cnt)

    for num in range(1,17):
        if not fish[num]: continue

        y,x,dir = fish[num]
        for _ in range(9):
            ny,nx = y+dy[dir],x+dx[dir]
            if ny>=0 and nx>=0 and ny<4 and nx<4 and not (ny==sy and nx==sx):
                fish[num][2] = dir
                break
            dir = (dir+1)%8
        else:
            continue

        swap(ny,nx,y,x)

    tmpspace, tmpfish = deepcopy(space), deepcopy(fish)
    tsy,tsx,tsd = sy,sx,sd

    for i in range(1,4):

        sy,sx = sy+dy[sd]*i,sx+dx[sd]*i
        if sy <0 or sx<0 or sy>=4 or sx>=4 or (not space[sy][sx]):
            sy,sx = tsy,tsx
            continue

        fish_num = space[sy][sx]
        sd = fish[fish_num][2]
        space[sy][sx]=[]
        fish[fish_num]=[]

        dfs(cnt+fish_num)

        space, fish = deepcopy(tmpspace), deepcopy(tmpfish)
        sy,sx,sd = tsy,tsx,tsd


dfs(first)
print(most)