from collections import defaultdict
from itertools import combinations
import re
from bisect import bisect_left


def solution(info, query):
    score_dict = defaultdict(list)
    t = [list(combinations([0, 1, 2, 3], num)) for num in range(1, 5)]

    for inf in info:
        info_list = inf.split(" ")
        score = int(info_list[-1])

        inf = info_list[:-1]

        label = ''.join(inf)

        score_dict[label].append(score)

        for idx in range(0, 4):
            for com in t[idx]:
                tmp = inf[:]
                for idx in com:
                    tmp[idx] = '-'
                label = ''.join(tmp)
                score_dict[label].append(score)

    for key in score_dict.keys():
        score_dict[key].sort()
    answer = []

    for q in query:
        q = re.sub(' and ', ' ', q)
        q = q.split(' ')
        score = int(q[-1])
        q_inf = q[:-1]

        label = ''.join(q_inf)
        a = score_dict[label]
        if label not in score_dict.keys():
            answer.append(0)
        else:
            cnt = len(a) - bisect_left(a, score)
            answer.append(cnt)

    return answer