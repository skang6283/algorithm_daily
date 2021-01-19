#graph layering timeout or bad implementtaion.
import sys
from heapq import *

input = sys.stdin.readline
N,E=map(int,input().split())
edges=[[[] for _ in range(N+1)] for _ in range(3)]

for _ in range(E):
    a,b,w=map(int,input().split())
    for i in range(3):
        edges[i][a].append((i,b,w))

v1,v2=map(int,input().split())

edges[0][v1].extend(edges[1][v1][:])
edges[0][v2].extend(edges[1][v2][:])
edges[1][v1].extend(edges[2][v1][:])
edges[1][v2].extend(edges[2][v2][:])


def dijkstra():
    spt = [[sys.maxsize]*(N+1) for _ in range(3)]
    spt[0][1]=0
    h=[(0,0,1)]

    while h:
        curd,curg,curv = heappop(h)

        if curd > spt[curg][curv]: continue

        for nextg, nextv, weight in edges[curg][curv]:
            oldd = spt[curg][curv]
            newd= curd + weight

            if newd > oldd:
                spt[nextg][nextv]= newd
                heappush(h,(newd,nextg,nextv))

    return spt
spt = dijkstra()
if spt[2][N] == sys.maxsize:
    print(-1)
else:
    print(spt[2][N])










