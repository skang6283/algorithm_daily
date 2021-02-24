def solution(s):
    answer = []

    s = s.replace("{", "").split("}")
    s = list(filter(None, s))

    val = []
    for l in s:
        val.append(list(filter(None, l.split(','))))

    val.sort(key=len)

    answer.append(val[0][0])
    for l in val:
        for num in l:
            if num not in answer:
                answer.append(num)

    answer = [int(n) for n in answer]
    return answer