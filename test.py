from collections import deque
import copy
import sys

answer=sys.maxsize
def bfs(start,end,graph,traps):
    global answer
    q=deque()
    q.append((start,graph,0))
    while q:
        fr,graph,p = q.popleft()
        if p>=answer:continue

        for to,price,dir in graph[fr]:
            if dir == 0:
                if to == end:
                    answer = min(answer, p+price)
                    continue
                if to in traps:
                    new_g = copy.deepcopy(graph)

                    for i in range(len(new_g[to])):
                        b,pp,dir = new_g[to][i]
                        new_g[to][i][2] = 1- dir
                        for i in range(len(new_g[b])):
                            if new_g[b][i][0]==to:
                                new_g[b][i][2] = 1-new_g[b][i][2]

                    q.append((to,new_g,p+price))
                else:
                    q.append((to,graph,p+price))



def solution(n, start, end, roads, traps):
    graph=[[] for _ in range(n)]
    traps = set([t-1 for t in traps])

    for fr,to,price in roads:
        graph[fr-1].append([to-1,price,0])
        graph[to-1].append([fr-1,price,1])

    start-=1
    end-=1
    bfs(start,end,graph,traps)

    return answer


#a = solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])

a= solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])
print(a)