from collections import deque

def bfs():
    q = deque([1])
    visited= set([1])

    while q:
        cur = q.popleft()

        for node in network[cur]:
            if node not in visited:
                visited.add(node)
                q.append(node)
    return visited

n = int(input()) # number of computers
m = int(input()) # edges
network = [[] for i in range(n+1)]
for i in range(m):
    a,b= [int(x) for x in input().split()]
    network[a].append(b)
    network[b].append(a)


print(len(bfs())-1)
