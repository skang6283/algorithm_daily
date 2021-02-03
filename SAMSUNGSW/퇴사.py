import sys

input = sys.stdin.readline

N = int(input())
sched=[]
ans =0
for _ in range(N):
    t,p = map(int,input().split())
    sched.append([t,p])

def dfs(day,earned):
    global ans
    if day >= N:
        ans = max(ans,earned)
        return
    t,p = 0,1
    T,P = sched[day][t],sched[day][p]

    if day+T <= N:
        dfs(day+T,earned+P)
    dfs(day+1,earned)


dfs(0,0)
print(ans)

