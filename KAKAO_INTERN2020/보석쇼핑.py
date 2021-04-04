from collections import defaultdict



def solution(gems):
    candidates=[]
    start,end=0,0

    unique=len(set(gems))
    d=defaultdict(lambda: 0)
    d[gems[0]]+=1
    while start<len(gems) and end<len(gems):
        print(start, end)
        print((d))

        if len(d) == unique:
            candidates.append((start,end))
            print(start,end)
            d[gems[start]] -= 1
            if d[gems[start]] == 0:
                d.pop(gems[start])
            start+=1

        else:
            end+=1
            if end<len(gems):
                d[gems[end]]+=1



    small=len(gems)
    for start,end in candidates:
        if abs(end-start)<small:
            small=abs(end-start)
            astart,aend = start,end


    return [astart+1,aend+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]				))