from collections import deque


def solution(n, edge):
    answer = 0

    edges = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        edges[v1].append(v2)
        edges[v2].append(v1)

    visited = set()
    c = [0] * (n + 1)
    q = deque()
    q.append((1, 0))
    visited.add(1)
    mx = 0
    while q:
        curv, cost = q.popleft()

        for neighbor in edges[curv]:
            if neighbor not in visited:
                visited.add(neighbor)
                if cost == mx:
                    mx = cost + 1
                c[neighbor] = cost + 1
                q.append((neighbor, cost + 1))

    for cc in c:
        if cc == mx:
            answer += 1

    return answer