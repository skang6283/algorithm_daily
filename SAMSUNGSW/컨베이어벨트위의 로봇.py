import sys
from collections import deque

input = sys.stdin.readline

N,K=map(int,input().split())
A = (list(map(int,input().split())))
A = deque([[i,0] for i in A])         #[내구도, 박스유]
box_loc = deque([])                   # 박스의 위치

box_num=0
def rotate():
    A.appendleft(A.pop())
    for i in range(len(box_loc)):
        box_loc[i] += 1

def clearN():
    if box_loc:
        if box_loc[0] == N-1:
            box_loc.popleft()
            A[N-1][1] = 0


def go():
    global box_num,K
    rotate()
    clearN()

    for num in range(len(box_loc)):
        loc = box_loc[num]

        if A[loc+1][1] == 0 and A[loc+1][0] >=1:
            A[loc][1], A[loc+1][1] = 0, 1
            A[loc+1][0] -= 1
            box_loc[num] = loc + 1
            if A[loc+1][0] == 0:
                K -=1

    clearN()

    if A[0][0] != 0 and A[0][1] == 0:
        A[0][1] = 1
        box_loc.append(0)
        A[0][0] -=1
        if A[0][0] == 0:
            K -= 1

    if K<=0:
        return 1
    return 0

cnt=0
while True:
    cnt+=1

    if go():
        break

print(cnt)