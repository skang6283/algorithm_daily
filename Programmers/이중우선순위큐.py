from heapq import *


def solution(operations):
    deleted = set()
    maxheap = []
    minheap = []
    for op in operations:
        cmd, num = op.split(' ')
        num = int(num)

        if cmd == 'D':
            if num == 1:
                while True:
                    if maxheap:
                        a = heappop(maxheap)
                        if a not in deleted:
                            deleted.add(-a)
                            break
                    else:
                        break

            else:
                while True:
                    if minheap:
                        a = heappop(minheap)
                        if a not in deleted:
                            deleted.add(a)
                            break
                    else:
                        break
        else:
            heappush(maxheap, -num)
            heappush(minheap, num)

    maxheap = list(set(maxheap) - set([-num for num in deleted]))
    minheap = list(set(minheap) - set(deleted))

    heapify(maxheap)
    heapify(minheap)

    answer = [0, 0]

    if maxheap and minheap:
        answer = [-heappop(maxheap), heappop(minheap)]

    if maxheap and not minheap:
        mx = -heappop(maxheap)
        answer = [mx, mx]

    if not maxheap and minheap:
        mn = heappop(maxheap)
        answer = [mn, mn]

    return answer