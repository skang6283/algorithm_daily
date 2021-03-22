from collections import defaultdict, deque


def solution(tickets):
    answer = ['ICN']
    total = len(tickets)+1

    d = defaultdict(list)
    for src, dest in tickets:
        d[src].append(dest)

    print(d)

    for key in d.keys():
        d[key] = deque(sorted((d[key])))
    cur = 'ICN'


    while True:
        new = d[cur].popleft()
        print(cur,new)
        if len(answer) ==total-1:
            answer.append(new)
            break

        if new not in d.keys():
            d[cur].append(new)
            continue
        else:
            cur = new

        answer.append(cur)



    return answer

a=[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(solution(a))