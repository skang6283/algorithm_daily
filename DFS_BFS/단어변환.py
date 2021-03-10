from collections import deque

def possible(a,b):
    cnt=0
    for al,bl in zip(a,b):
        if al != bl:
            cnt +=1
    if cnt ==1:
        return True
    return False

def bfs(begin,target,words):
    q = deque()

    v=set()
    v.add(begin)

    q.append((begin,v))

    while q:
        current,visited= q.popleft()
        print(current)
        if current == target:
            return len(visited)-1
            break

        for w in words:
            if w not in visited and possible(w,current):
                new = visited.copy()
                new.add(w)
                q.append((w, new))

    return 0



def solution(begin, target, words):
    if target not in words:
        return 0

    answer=bfs(begin,target,words)

    return answer