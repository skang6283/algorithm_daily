import sys

input = sys.stdin.readline
R,C,M=map(int,input().split())
sharks =[[[0,0,0] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    sharks[r-1][c-1]=[s,d,z]

dy=[-1,1,0,0]
dx=[0,0,1,-1]




# r, c, s, d, z
# (r, c)는 상어의 위치,
# s는 속력,
# d는 이동 방향,
# z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽

def get(x):
    for y in range(R):
        if sharks[y][x][2]:
            a = sharks[y][x][2]
            sharks[y][x]=[0,0,0]
            return a
    return 0

def smove():
    tmp =[[[0,0,0] for _ in range(C)] for _ in range(R)]

    global sharks
    for y in range(R):
        for x in range(C):
            if not sharks[y][x][2]: continue

            ts,d,z = sharks[y][x]
            s=ts
            ny,nx = y,x

            while s:
                # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽

                ny=ny+dy[d-1]
                nx=nx+dx[d-1]

                s -=1
                if ny<0:
                    d+=1
                    s+=2
                elif ny>=R:
                    d-=1
                    s+=2
                elif nx<0:
                    s+=2
                    d-=1
                elif nx>=C:
                    s+=2
                    d+=1

            if tmp[ny][nx][2]< z:
                tmp[ny][nx]=[ts,d,z]
    sharks=tmp

def pt(t):
    print("tmp")
    for a in t:
        print (a)
    print()
def ps():
    print("sharks")
    for a in sharks:
        print (a)
    print()

cnt=0
for i in range(C):
    cnt+=get(i)
    smove()
print(cnt)
