# a: 0:기둥 1:보
# b: 0:삭제 1:설치

n,M = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(M)]

print(s)
def pp(bo,col,n):
    print("보                    기둥")
    for i in range(n,-1,-1):
        for j in range(n+1):
            print(bo[j][i], end=' ')
        print("  ", end=" ")
        for j in range(n + 1):
            print(col[j][i],end=' ')
        print()
    print()

def delete(x, y, a, bo, col, n):
    if a == 0:
        col[x][y] = 0
    else:
        bo[x][y] = 0

    flag=0
    for i in range(n+1):
        for j in range(n+1):
            if bo[i][j] == 1:
                if not check(i, j, 1, bo, col,n):
                    flag=1
            if col[i][j] == 1:
                if not check(i, j, 0, bo, col,n):
                    flag=1

    if flag:
        if a == 0:
            col[x][y] = 0
        else:
            bo[x][y] = 1



def check(x, y, a, bo, col,n):
    if a == 0:  # 기둥
        if y==0 or col[x][y-1]==1:
            return 1

        if x == 0:
            if bo[x][y] == 1:
                return 1
        else:
            if bo[x-1][y] ==1 or bo[x][y] ==1:
                return 1
    else:  # 보
        if x == 0 or x == n - 1:
            if col[x][y - 1] == 1 or col[x + 1][y - 1]==1:
                return 1
        else:
            if col[x][y - 1] == 1 or col[x + 1][y - 1] == 1 or (bo[x - 1][y] == 1 and bo[x + 1][y] == 1):
                return 1
    pp(bo,col,n)
    print("fail: ",x,y,a)
    return 0


def solution(n, build_frame):
    answer = []
    frames = []
    bo = [[0] * (n+1) for _ in range(n+1)]
    col = [[0] * (n+1) for _ in range(n+1)]

    for x, y, a, b in build_frame:
        if not b:
            delete(x,y,a,bo, col, n)
        else:
            if a:
                bo[x][y] = check(x, y, a, bo, col,n)
            else:
                col[x][y] = check(x, y, a, bo, col,n)

    for i in range(n+1):
        for j in range(n+1):
            if col[i][j]:
                answer.append([i, j, 0])
            if bo[i][j]:
                answer.append([i, j, 1])

    return answer

print(solution(n,s))

# 5 8
# 1 0 0 1
# 1 1 1 1
# 2 1 0 1
# 2 2 1 1
# 5 0 0 1
# 5 1 0 1
# 4 2 1 1
# 3 2 1 1

# 5 10
# 0 0 0 1
# 2 0 0 1
# 4 0 0 1
# 0 1 1 1
# 1 1 1 1
# 2 1 1 1
# 3 1 1 1
# 2 0 0 0
# 1 1 1 0
# 2 2 0 1

