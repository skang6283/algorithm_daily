from collections import deque

def bfs(node,graph):
    q= deque()
    q.append((node,-1,0))
    win_cnt,lose_cnt=0,0
    visited=set()
    visited.add(node)
    while q:
        cur, dir,cnt = q.popleft()
        for b,d in graph[cur]:
            if b in visited: continue
            if dir==-1:
                visited.add(b)
                q.append((b,d,cnt+1))
                if d==1:
                    win_cnt+=1
                else:
                    lose_cnt+=1
            else:
                if dir==d:
                    visited.add(b)
                    q.append((b,d,cnt+1))

                    if d == 1:
                        win_cnt += 1
                    else:
                        lose_cnt += 1

    return win_cnt,lose_cnt

def solution(n, results):
    answer = 0

    graph=[[] for _ in range(n)]
    print(graph)
    for a,b in results:
        graph[a-1].append([b-1,1])  # 1 a wins b
        graph[b-1].append([a-1,0])  # 0 b loses to a


    answer=0
    for i in range(n):
        w,l = bfs(i,graph)
        print(w,l)
        if w+l==n-1:
            answer+=1


    return answer



a=solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	)
print(a)