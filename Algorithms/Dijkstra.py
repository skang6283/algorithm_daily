# Find shortest path from starting vertex to every other vertex in the graph

# Time complexity
# O(V + E log V) with min-priority queue

from heapq import *
import sys
INF = sys.maxsize

N= int(input())

def dijstra(start):
    dist = [INF] * (N+1)    # list to store current distance from start to node
    h = [(0,start)]         # heapq to find the shortest distance from start node

    dist[start]=0           # from start to start is 0


    while h:
        curd, curv = heappop(h)             # get the vertex with the shortest distance from start
        if curd > dist[curv]: continue      # that has not been visited

        for nextv, weight in edges[curv]:   # for its neigbors
            newd = curd + weight            # calculate te new distance
            oldd = dist[nextv]              # get the old distance
            if newd < oldd:                 # if new distance is smaller than the old distance
                dist[nextv]=newd            # update the distance, and push it to the heap
                heappush(h,(newd,nextv))
    return dist