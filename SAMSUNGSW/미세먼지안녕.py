import sys

input = sys.stdin.readline
R,C,T = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(R)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]

filtery,filterx=0,0
flag=0

for i in range(R):
    if flag:
        break
    for j in range(C):
        if room[i][j]== -1:
            filtery, filterx = i, j
            flag=1
            break

def spread():
    tmp=[[0]*C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if room[y][x]== -1 or room[y][x]==0: continue       # no dust or filter

            dust = room[y][x]
            cnt=0
            tospread=[]
            for i in range(4):
                ny,nx = y+dy[i],x+dx[i]
                if ny<0 or nx<0 or ny>= R or nx >=C or room[ny][nx]==-1: continue
                tospread.append((ny,nx))
                cnt +=1

            amount = dust // 5              #확산되는양
            leftover = dust - amount*cnt    #남는양
            room[y][x] = leftover
            for ny,nx in tospread:
                tmp[ny][nx] +=amount

    for y in range(R):
        for x in range(C):
            room[y][x]+=tmp[y][x]
def startFilter():
    #up
    for i in range(filtery-1,0,-1):                    #v
        room[i][0]=room[i-1][0]

    for i in range(0,C-1):                          #<--
        room[0][i] = room[0][i+1]

    for i in range(0,filtery):                    #^
        room[i][C-1] = room[i+1][C-1]

    for i in range(C-1,0,-1):                       #-->
        if room[filtery][i-1]==-1:
            room[filtery][i]=0
        else:
            room[filtery][i] = room[filtery][i-1]



    #down
    for i in range(filtery+2,R-1 ):                 #^
        room[i][0] = room[i + 1][0]

    for i in range(0, C - 1):                       #<--
        room[R-1][i] = room[R-1][i + 1]

    for i in range(R-1, filtery+1,-1):                #v
        room[i][C - 1] = room[i - 1][C - 1]

    for i in range(C - 1, 0, -1):                   #-->
        if room[filtery+1][i - 1] ==-1:
            room[filtery + 1][i] =0
        else:
            room[filtery+1][i] = room[filtery+1][i - 1]



def proom():
    for a in room:
        print(a)
    print()

def count():
    cnt=0
    for i in range(R):
        for j in range(C):
            if room[i][j]==-1: continue
            cnt += room[i][j]
    return cnt


for _ in range(T):
    spread()
    startFilter()

print(count())



