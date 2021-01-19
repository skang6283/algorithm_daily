import sys
from collections import deque

input = sys.stdin.readline
circle = [deque(map(int,input().strip())) for _ in range(4)]
# N = 0 , S = 1
K= int(input())
rotate = [list(map(int,input().split())) for _ in range(K)]

def roll(num,d):
    if d == 1: # 1 : c wise
        temp = circle[num].pop()
        circle[num].appendleft(temp)

    if d == -1: # : cc wise
        temp = circle[num].popleft()
        circle[num].append(temp)


def bfs(num,d):
    visited=[False]*4
    visited[num] = True

    q = deque()
    q.append((num,d))

    dall=[0]*4
    dall[num]=d

    while q:
        cnum, cd = q.popleft()

        if (cnum-1) >= 0 and not visited[cnum-1]:
            if circle[cnum][6] != circle[cnum-1][2]:
                q.append((cnum-1,-cd))
                dall[cnum-1]= -cd
                visited[cnum-1]= True

        if (cnum+1) < 4 and not visited[cnum+1]:
            if circle[cnum][2] !=circle[cnum+1][6]:
                q.append((cnum+1,-cd))
                dall[cnum+1]= -cd
                visited[cnum+1]= True

    for i in range(len(dall)):
        roll(i,dall[i])

for a,b in rotate:
    bfs(a-1,b)

print(circle[0][0]+circle[1][0]*2+circle[2][0]*4+circle[3][0]*8)





