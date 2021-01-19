import sys

input = sys.stdin.readline
N,L = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(N)]

visited = [False]*N



def check(line):
    for i in range(len(line)-1):
        if abs(line[i]-line[i+1]) >1:
            return 0

        if (line[i]-line[i+1]) ==1:
            for j in range(L):

                if  (i+1+j)>=N or visited[i+1+j]:

                    return 0
                visited[i+1+j]=True

        if (line[i] - line[i + 1]) == -1:
            for j in range(L):
                if (i-j)<0 or visited[i-j]:
                    return 0
                visited[i - j] =True

    return 1

cnt=0

for a in road:
    cnt+=check(a)
    visited = [False] * N

transposed =[]
for a in zip(*road):
    transposed.append(list(a))

for a in transposed:
    cnt+=check(a)
    visited = [False] * N

print(cnt)

