from collections import deque


def solution(number, k):
    answer = []

    string_list = deque(list(str(number)))

    while k:
        if not string_list:
            break
        if not answer:
            answer.append(string_list.popleft())
        else:
            if string_list[0] > answer[-1]:
                answer.pop()
                k -= 1
            else:
                answer.append(string_list.popleft())

    answer = "".join(answer[:(len(answer) - k)]) + "".join(string_list)

    return answer