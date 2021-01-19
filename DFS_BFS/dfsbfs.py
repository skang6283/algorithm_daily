from collections import deque

# deque popleft takes O(1)
# while list pop(0) take O(n), use deque for queue operation

def dfsUtil(v,visited):
    print(v, end=" ")
    visited.add(v)
    for node in graph[v]:
        if node not in visited:
            dfsUtil(node,visited)

def dfs(v):
    visited = set()
    dfsUtil(v,visited)

def bfs(v): # queue
    visited=set()
    q = deque([v])
    visited.add(v)
    while q:
        current = q.popleft()
        print(current, end=" ")
        for node in graph[current]:
            if node not in visited:
                q.append(node)
                visited.add(node)


n,m,v=[int(x) for x in input().split()]
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

for a in graph:
    a.sort()


dfs(v)
print()
bfs(v)