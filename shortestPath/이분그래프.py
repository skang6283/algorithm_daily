#이분그래프 = bipartite
import sys
from heapq import *
from collections import defaultdict

V,E = map(int,sys.stdin.readline().split())
start= int(sys.stdin.readline().strip())

weights = defaultdict(list)
neighbors = [[] for _ in range(V+1)]

for _ in range(E):
    s,end,w = map(int,sys.stdin.readline().split())
    weights[(s,end)].append(w)
    neighbors[s].append(end)

for key in weights:
    weights[key] = min(weights[key])

def dijkstra(s_in):
    spt = [sys.maxsize]*(V+1)
    spt[s_in]= 0
    h = [(0,s_in)]

    while h:
        dist,curv = heappop(h)
        if dist > spt[curv]: continue

        for nextv in neighbors[curv]:
            oldd = spt[nextv]
            newd = dist+weights[(curv,nextv)]

            if newd < oldd:
                heappush(h,(newd,nextv))
                spt[nextv]= newd




    return spt

spt = dijkstra(start)
for i in range(1,len(spt)):
    if spt[i] == sys.maxsize:
        print('INF')
    else:
        print(spt[i])




# 5 7
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 2 4 3
