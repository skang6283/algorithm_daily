from collections import deque


def solution(n, edge):
    answer = 0

    edges = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        edges[v1].append(v2)
        edges[v2].append(v1)

    print(edges)
    visited = []
    q = deque()
    q.append((1,0))
    while q:
        print(q)
        curv, cost = q.popleft()

        print("asdfasd")
        for neighbor in edges[curv]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.append((neighbor, cost + 1))
    return answer


a = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(6,a)