import sys
from collections import deque

input = sys.stdin.readline

N,M,T = map(int,input().split())

circle = [deque(list(map(int,input().split()))) for _ in range(N)]
rotate =[]
for _ in range(T):
    x,d,k = map(int,input().split())
    rotate.append([x,d,k])

# x    의 배수인 원판
# d.   0:c  1:cc
# k    회전수

# 인접하고 같은수를 지움
# 없는 경우 원판에 적힌 수의 평균을 구하고, 평균보다 큰수에 -1 작은수에는 +1는

def go(x,d,k):
    for i in range(1,N):
        if (i+1) % x != 0: continue
        for _ in range(k):
            if d: #cc
                circle[i].append(circle[i].popleft())
            else:   #c
                circle[i].appendleft(circle[i].pop())

    same=set()
    flag=0
    idx=[i for i in range(M)]
    for i in range(N):
        for j in range(M):
            cur = circle[i][j]

            if cur == 'x': continue

            left,right = (i,idx[j-1]),(i,idx[(j+1)%M])

            if cur == circle[left[0]][left[1]]:
                same.add(left)
                flag=1
            if cur == circle[right[0]][right[1]]:
                same.add(right)
                flag=1

            if i-1 >=0:     # down
                if cur == circle[i-1][j]:
                    same.add((i-1,j))
                    flag=1
            if i+1 <N:      # up
                if cur == circle[i+1][j]:
                    same.add((i+1,j))
                    flag=1

    #debug()
    if not flag:
        num, cnt = 0, 0
        #print("no  such number")
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 'x':
                    num += circle[i][j]
                    cnt +=1
        if cnt ==0:
            return 1
        avg = num / cnt

        #print(avg)
        for i in range(N):
            for j in range(M):
                if circle[i][j] == 'x': continue
                if circle[i][j] < avg:
                    circle[i][j] += 1
                elif circle[i][j] > avg:
                    circle[i][j] -= 1
    else:
        #print('found such number')
        for y,x in list(same):
            circle[y][x]= 'x'

    return 0
def debug():
    for i in range(N):
        for j in range(M):
            print(circle[i][j], end =" ")
        print()
    print()

def getsum():
    sum=0
    for i in range(N):
        for j in range(M):
            if circle[i][j] == 'x': continue
            sum += circle[i][j]
    return sum

#debug()
for x,d,k in rotate:
    if go(x,d,k):
        break

print(getsum())
