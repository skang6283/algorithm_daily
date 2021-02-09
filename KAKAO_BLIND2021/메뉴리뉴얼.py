from itertools import combinations, permutations
from collections import defaultdict


def solution(orders, course):
    total = [defaultdict(int) for _ in range(max(course) + 1)]
    maxlength = [0] * (max(course) + 1)
    answer = []

    for order in orders:
        for number in course:
            for candidate in list(combinations(order, number)):
                candidate = list(candidate)
                candidate = ''.join(sorted(candidate))
                if candidate:
                    total[number][candidate] += 1
                    maxlength[number] = max(maxlength[number], total[number][candidate])

    for number in course:
        search = maxlength[number]
        if search <= 1: continue
        for menu, cnt in total[number].items():
            if cnt == search:
                answer.append(menu)

    return sorted(answer)


## LEARN TO USE COUNTER