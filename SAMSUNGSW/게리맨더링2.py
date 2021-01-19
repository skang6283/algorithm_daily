import sys

input = sys.stdin.readline
N= int(input())

city = [list(map(int,input().split())) for _ in range(N)]

population = [[0]*N for _ in range(N)]


def divide(x,y,d1,d2):
    population = [[0] * N for _ in range(N)]
    m =[0]*5
    #print(x,y,d1,d2)

    # mark 1
    for i in range(x+d1-1):
        for j in range(y):
            if (i+j) < (x-1+y-1):
                m[0]+=city[i][j]
                population[i][j]=1
    # mark 2
    dy=y
    for i in range(x+d2):
        if i<x:
            for j in range(y, N):
                m[1]+=city[i][j]
                population[i][j] = 2
        if i>=x:
            dy+=1
            for j in range(y, N):
                if j>=dy:
                    m[1] += city[i][j]
                    population[i][j] = 2

    # mark 3
    dy = y-d1-1
    for i in range(x+d1-1,N):
        if i <x+d1+d2:
            for j in range(0,y-d1+d2-1):
                if j < dy:
                    m[2] += city[i][j]
                    population[i][j]=3
            dy+=1
        else:
            for j in range(0,y-d1+d2-1):
                m[2]+=city[i][j]
                population[i][j]=3

    # mark 4
    dy = y+d2-2
    for i in range(x + d2, N):
        if i <= x + d1 + d2 -1 :
            for j in range(y+d2-d1-1,N):
                if j > dy:
                    m[3] += city[i][j]
                    population[i][j] = 4
            dy -= 1
        else:
            for j in range(y+d2-d1-1,N):
                m[3]+=city[i][j]
                population[i][j] = 4

    #mark 5:
    for i in range(x-1,x+d1+d2):
        for j in range(y-d1-1,y+d2):
            if not population[i][j]:
                m[4] += city[i][j]
                population[i][j]=5

    # for a in population:
    #     print(a)
    # print(m)
    # print()
    return max(m)-min(m)

def pp():
    for a in population:
        print(a)

ans =sys.maxsize
for x in range(1,N-2):
    for y in range(2,N-1):
        for d1 in range(1,N-1):
            for d2 in range(1,N-1):
                if x+d1+d2<=N and 1<=y-d1 and y+d2 <=N:
                    #print(ans)
                    ans = min(ans,divide(x,y,d1,d2))

print(ans)



