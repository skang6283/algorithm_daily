from collections import deque

n= int(input())
s = [list(map(int,input().split())) for _ in range(n)]

def debug(cur1,cur2,board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (cur1[0] == i and cur1[1] == j) or (cur2[0] == i and cur2[1] == j):
                print("P", end = " ")
            else:

                print(board[i][j],end =" ")
        print()

def isPossible(y, x,board):
    n = len(board)
    if x < 0 or y < 0 or x >= n or y >= n or board[y][x] == 1:
        return False
    return True

def can(cur1,cur2,d,board,cnt):
    n = len(board)
    Y,X = 0,1
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    cans=[]

    #위 아래
    for dd in directions:
        new1 = (cur1[Y]+dd[Y], cur1[X]+dd[X])
        new2 = (cur2[Y] + dd[Y], cur2[X] + dd[X])
        if isPossible(new1[Y],new1[X],board) and isPossible(new2[Y],new2[X],board):
            cans.append((new1,new2,d,cnt+1))

    # 회전
    if d == 0 : # 가로
        if isPossible(cur1[Y]-1,cur1[X],board) and isPossible(cur2[Y]-1,cur2[X],board):
            cans.append((cur1, (cur1[Y] - 1,cur1[X]),1-d,cnt+1))
            cans.append((cur2, (cur2[Y] - 1, cur2[X]),1-d,cnt+1))
        if isPossible(cur1[Y]+1,cur1[X],board) and isPossible(cur2[Y]+1,cur2[X],board):
            cans.append((cur1, (cur1[Y] +1, cur1[X]),1-d,cnt+1))
            cans.append((cur2, (cur2[Y] +1, cur2[X]),1-d,cnt+1))

    else:
        if isPossible(cur1[Y],cur1[X]-1,board) and isPossible(cur2[Y],cur2[X]-1,board):
            cans.append((cur1, (cur1[Y],cur1[X]-1),1-d,cnt+1))
            cans.append((cur2, (cur2[Y], cur2[X]-1),1-d,cnt+1))
        if isPossible(cur1[Y],cur1[X]+1,board) and isPossible(cur2[Y],cur2[X]+1,board):
            cans.append((cur1, (cur1[Y],cur1[X]+1),1-d,cnt+1))
            cans.append((cur2, (cur2[Y], cur2[X]+1),1-d,cnt+1))
    return cans

def solution(board):

    N = len(board)
    q = deque()
    s1,s2=(0,0),(0,1)
    q.append([s1,s2, 0, 0])
    visited=set()
    visited.add((s1,s2))
    visited.add((s2,s1))

    while q:
        cur1,cur2,d,cnt = q.popleft()
        print("##########",cur1,cur2,d,cnt)
        debug(cur1,cur2,board)
        print("from",cur1,cur2,d,cnt)

        for pos in can(cur1,cur2,d,board,cnt):
            new1, new2 = pos[0],pos[1]
            if new1 == (N - 1, N - 1) or new2 == (N - 1, N - 1):
                return cnt+1
            if (pos[0],pos[1]) not in visited:
                print("covered:", new1, new2)

                q.append(pos)
                visited.add((pos[1],pos[0]))
                visited.add((pos[0],pos[1]))
    return -1


print(solution(s))

# 5
# 0 0 0 1 1
# 0 0 0 1 0
# 0 1 0 1 1
# 1 1 0 0 1
# 0 0 0 0 0

# 7
# 0 0 0 0 0 0 1
# 1 1 1 1 0 0 1
# 0 0 0 0 0 0 0
# 0 0 1 1 1 1 0
# 0 1 1 1 1 1 0
# 0 0 0 0 0 1 1
# 0 0 1 0 0 0 0