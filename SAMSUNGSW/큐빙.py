import sys
from collections import defaultdict
input = sys.stdin.readline
# 0, 1, 2, 3, 4, 5
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽
#    흰색,    노란색,        빨간색,  오렌지색, 초록색,  파란색

# + :c
# - :cc

# 큐브의 순환구조 인덱싱 방법
#      v
#    < ^ v
#      >
#      <


# Q,W,E,Z,X = ^,>,v,<,>
def go(side):
    global U,D,F,B,L,R
    if side == 'U':
        self, bottom, up, left, right = U,F,B,L,R
        temp = list(map(list, zip(*reversed(self))))
        U = temp[:]

    if side == 'D':
        self, bottom, up, left, right = D,R,L,B,F
        temp = list(map(list, zip(*reversed(self))))
        D = temp[:]

    if side == 'F':
        self, bottom, up, left, right = F,L,R,U,D
        temp = list(map(list, zip(*reversed(self))))
        F = temp[:]

    if side == 'B':
        self, bottom, up, left, right = B,D,U,R,L
        temp = list(map(list, zip(*reversed(self))))
        B = temp[:]

    if side == 'L':
        self, bottom, up, left, right = L,U,D,F,B
        temp = list(map(list, zip(*reversed(self))))
        L = temp[:]

    if side == 'R':
        self, bottom, up, left, right = R,B,F,D,U
        temp = list(map(list, zip(*reversed(self))))
        R = temp[:]


    tmp1,tmp2,tmp3 = bottom[0][0],bottom[1][0],bottom[2][0]
    bottom[0][0],bottom[1][0],bottom[2][0] = right[2][2],right[1][2],right[0][2]
    right[2][2], right[1][2], right[0][2] = up[0][2],up[0][1],up[0][0]
    up[0][2], up[0][1], up[0][0] = left[2][0],left[2][1],left[2][2]
    left[2][0], left[2][1], left[2][2] = tmp1,tmp2,tmp3

T = int(input())
rotate=[]
for i in range(T):
    N = int(input())
    rotate.append(list(map(str, input().split())))

for i in range(T):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]

    for s, d in rotate[i]:
        go(s)
        if d == '-':
            go(s)
            go(s)

    for a in U:
        print(*a, sep='')