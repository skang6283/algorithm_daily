from heapq import *
import sys


def solution(n, costs):
    INF = sys.maxsize

    c = [[] for _ in range(n)]
    for v1, v2, cost in costs:
        c[v1].append((v2, cost))
        c[v2].append((v1, cost))

    mst = []
    answer = [0] * n
    dist = {i: INF for i in range(n)}
    dist[0] = 0

    while len(mst) != n:
        curv = min(dist, key=dist.get)

        if curv in mst:
            dist[curv] = INF
            continue

        mst.append(curv)
        answer[curv] = dist[curv]
        for neighbor, cost in c[curv]:
            if cost < dist[neighbor]:
                dist[neighbor] = cost

    return sum(answer)