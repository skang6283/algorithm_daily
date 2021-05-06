from collections import deque

def solution(ads):
    answer = 0

    #sort by start time
    ads.sort(key = lambda x: x[0])

    remaining=deque()
    remaining.add(ads[0])

    for i in range(1,len(ads)):
        start,cost = remaining[0]
        next_start,next_cost=ads[i]

        first_waiting_cost = (next_start-start+5)*cost
        next_waiting_cost = (start+5-next_start)*next_cost

        if first_waiting_cost>next_waiting_cost

    return answer