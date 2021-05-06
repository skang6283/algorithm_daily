from collections import deque
def solution(n, path, order):
    visited=[0]*n
    cave=[set() for _ in range(n)]


    for a,b in path:
        cave[a].add(b)
        cave[b].add(a)

    before=[0]*n
    after=[-1]*n
    for start,end in order:
        visited[start] = 0
        before[end] = start
        after[start] = end


    if before[0] != 0:
        return False

    q=deque()
    visited[0]=1
    q.append(0)
    repeat=0
    prev=-1
    while q:
        repeat+=1
        cur = q.popleft()
        print(cur)
        for neighbor in cave[cur]:
            if not visited[neighbor] and visited[before[neighbor]]: # before is visited
                visited[neighbor] = 1
                q.append(neighbor)

                if after[neighbor] != -1:
                    if visited[after[neighbor]] == 2:
                        visited[after[neighbor]] = 1
                        q.append(after[neighbor])

            else: # before is not visited
                visited[neighbor] = 2

        print(visited)
        if repeat>=100:
            break


    for v in visited:
        if v==0:
            return False

    return True




#a =solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]) # True
#a =solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]) # True
a = solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]) # False

print(a)