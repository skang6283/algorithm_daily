import sys
from heapq import *

INF = sys.maxsize
input= sys.stdin.readline

N,E=map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,w = map(int, input().split())
    edges[a].append((b,w))
    edges[b].append((a,w))
v1,v2 = map(int,input().split())



def dijstra(start):
    dist = [INF] * (N+1)
    h = [(0,start)]
    dist[start]=0

    while h:
        curd, curv = heappop(h)

        if curd > dist[curv]: continue

        for nextv, weight in edges[curv]:
            newd = curd + weight
            oldd = dist[nextv]
            if newd < oldd:
                dist[nextv]=newd
                heappush(h,(newd,nextv))
    return dist

d1 = dijstra(1)
d2 = dijstra(v1)
d3 = dijstra(v2)

# 1 - v1 - v2 - N
# 1 - v2 - v1 - N
flag1,flag2=0,0
if d1[v1] != INF and d2[v2] != INF and d3[N] != INF:
    ans1=d1[v1]+d2[v2]+d3[N]
else:
    flag1 = 1

if d1[v2] != INF and d3[v1] != INF and d2[N] != INF:
    ans2=d1[v2]+d3[v1]+d2[N]
else:
    flag2 = 1


if flag1 == 1 and flag2 == 1:
    print(-1)
else:
    print(min(ans1,ans2))


