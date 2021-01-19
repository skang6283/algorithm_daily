N,M= map(int,input().split())
key = [list(map(int,input().split())) for _ in range(M)]
lock = [list(map(int,input().split())) for _ in range(N)]


def check(locktable, M, N):
    for i in range(N):
        for j in range(N):
            if locktable[M + i - 1][M + j - 1] != 1:
                return False;
    return True


def tryFit(sy, sx, key, locktable, M, N):
    prev = [[0] * M for _ in range(M)]
    flag = True
    for i in range(M):
        for j in range(M):
            prev[i][j] = locktable[sy + i][sx + j]
            if locktable[sy + i][sx + j] != key[i][j]:
                locktable[sy + i][sx + j] = 1
            else:
                locktable[sy + i][sx + j] = 0

    if check(locktable, M, N):
        return True

    for i in range(M):
        for j in range(M):
            locktable[sy + i][sx + j] = prev[i][j]

    return False


def desert(sy, sx, prev, locktable, M):
    for i in range(M):
        for j in range(M):
            locktable[sy + i][sx + j] = prev[i][j]


def solution(key, lock):
    M = len(key)
    N = len(lock)

    bigN = N + (M - 1) * 2
    locktable = [[0] * bigN for _ in range(bigN)]

    for i in range(N):
        for j in range(N):
            locktable[M + i - 1][M + j - 1] = lock[i][j]

    for i in range(4):
        key = list(zip(*reversed(key)))

        for sy in range(N + M - 1):
            for sx in range(N + M - 1):
                if tryFit(sy, sx, key, locktable, M, N):
                    return True

    return False


solution(key,lock)
# 3 3
# 0 0 0
# 1 0 0
# 0 1 1
# 1 1 1
# 1 1 0
# 1 0 1