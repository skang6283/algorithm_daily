import sys
from heapq import *

INF = sys.maxsize


def dijstra(n, start, road):
    dist = [INF] * n
    dist[start]=0
    h = [(0, start)]

    while h:
        curd, curv = heappop(h)

        if curd > dist[curv]: continue
        for next, fare in road[curv]:
            newfare = curd + fare
            oldfare = dist[next]
            if newfare < oldfare:
                dist[next] = newfare
                heappush(h, (newfare, next))

    return dist


def solution(n, s, a, b, fares):
    road = [[] for _ in range(n)]
    dist = [[] for _ in range(n)]
    s -= 1; a -= 1; b -= 1;
    answer = sys.maxsize
    for v1, v2, fare in fares:
        road[v1 - 1].append((v2-1, fare))
        road[v2 - 1].append((v1-1, fare))

    for v in range(n):
        dist[v] = dijstra(n, v, road)
        print(dist[v])

    for mid in range(n):
        answer = min(answer,dist[s][mid] + dist[mid][a] + dist[mid][b])

    return answer


n,s,a,b = map(int,input().split())
fares = input()
fares = eval(fares)

answer = solution(n,s,a,b,fares)
print(answer)