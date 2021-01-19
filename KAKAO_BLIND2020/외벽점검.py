import sys
from itertools import permutations
from heapq import *
from collections import deque

input = sys.stdin.readline

answer = sys.maxsize

n = int(input())
weak = list(map(int,input().split()))
dist = list(map(int,input().split()))

#####################
# using permutation #
#####################
def solution(n, weak, dist):

    dist.sort(reverse=True)
    weakpoints = weak + [n+ w for w in weak]
    L = len(weak)
    cand =[]
    for start_index in range(len(weak)):
        for friends in permutations(dist):

            cur = weak[start_index]
            for cnt,f in enumerate(friends):
                cur +=f
                if cur < weakpoints[start_index+L-1]:
                    cur = [w for w in weakpoints[start_index+1:start_index+L] if w >cur][0]
                else:
                    cand.append(cnt+1)
                    break
    print(cand)


    return min(cand) if cand else -1


def solution2(n, weak, dist):

    dist.sort(reverse=True)
    q =deque()
    q.append(weak)



    for i,d in enumerate(dist):
        for _ in range(len(q)):
            cur = q.popleft()
            print("##############", cur)
            for start_index in range (len(cur)):
                start = cur[start_index]
                end = (start + d) % n

                if start < end:
                    notv = list(filter(lambda x : x < start or x > end,cur))
                else:
                    notv = list(filter(lambda x : x > start and x < end,cur))

                print(i, d,start,notv)
                if not notv:
                    return i+1
                else:
                    q.append(notv)

    answer = -1

    return answer

print(solution2(n,weak,dist))


# 12
# 1 5 6 10
# 1 2 3 4

# 12
# 1 3 4 9 10
# 3 5 7