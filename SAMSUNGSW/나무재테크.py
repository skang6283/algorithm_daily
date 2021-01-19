import sys
from collections import deque

input = sys.stdin.readline

N,M,K = map(int,input().split())
A= [list(map(int,input().split())) for _ in range(N)]
trees={(i,j): deque() for i in range(N) for j in range(N)}


# initial sort
tmp=[[[]for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,z= map(int,input().split())
    tmp[x-1][y-1].append(z)

for i in range(N):
    for j in range(N):
        tmp[i][j].sort()
        trees[(i,j)] = deque(tmp[i][j])

ingredient =[[5]*N for _ in range(N)]

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

# 봄 = 나이만큼 양분 섭취 후 나이++, 나이가 어린 나무부터 양분섭취, 부족할시 즉사
# 여름 = 봄에 죽은 나무나이/2 가 양분으로 추가
# 가을 = 번식, 나무나이가 5의 배수일시 인접한칸에 나무생성
# 겨울 = 양분추가

def spring():
    dead=[]

    for (x,y), ages in trees.items():
        survived = deque()
        for age in ages:
            if ingredient[x][y]<age:
                dead.append((x,y,age))
            else:
                ingredient[x][y]-=age
                survived.append(age+1)
        trees[(x,y)] = survived
    return dead

def summer(dead):
    for x,y,age in dead:
        ingredient[x][y] += age//2

def fall():
    tmp =[[0]*N for _ in range(N)]
    for (x,y), ages in trees.items():
        for age in ages:
            if age%5==0:
                for i in range(8):
                    nx,ny=x+dx[i],y+dy[i]
                    if nx<0 or ny<0 or nx>=N or ny >=N: continue
                    tmp[nx][ny]+=1

    for i in range(N):
        for j in range(N):
            for k in range(tmp[i][j]):
                trees[(i,j)].appendleft(1)


def winter():
    for i in range(N):
        for j in range(N):
            ingredient[i][j] += A[i][j]

def count():
    cnt=0
    for i in range(N):
        for j in range(N):
            cnt += len(trees[(i, j)])
    return cnt
for i in range(K):
    dead = spring()
    summer(dead)
    fall()
    winter()

print(count())
