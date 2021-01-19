#상 하 좌 우
from collections import deque

def bfs(y,x):
    global n
    q = deque([(y,x)])
    visited.add((y,x))
    count=1

    while q:
        cury, curx = q.popleft()
        for i in range(4):
            newy = cury + dy[i]
            newx = curx + dx[i]
            if newy>=0 and newx>=0 and newy < n and newx <n:
                if map[newy][newx] =='1' and (newy,newx) not in visited:
                    q.append((newy,newx))
                    visited.add((newy, newx))
                    count += 1

    return count


dx=[0,0,-1,1]
dy=[-1,1,0,0]

n = int(input())
map=[input() for i in range(n)]
visited=set()
result=[]
for y in range(n):
    for x in range(n):
        if map[y][x] == '1' and (y,x) not in visited:
             result.append(bfs(y,x))

print(len(result))
for a in sorted(result):
    print(a)