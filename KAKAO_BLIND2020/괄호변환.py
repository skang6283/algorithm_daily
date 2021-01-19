from collections import deque

s= input()

def check(v):
    t = deque(v)
    cnt = 0
    while t:
        if cnt < 0:
            return False
        if t.popleft() == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt != 0:
        return False
    return True


def divde(arr):
    t = deque(arr)
    u, v = '', ''
    cnt = 0
    while t:
        if t.popleft() == '(':
            cnt += 1
            u += '('
        else:
            cnt -= 1
            u += ')'

        if cnt == 0:
            break

    while t:
        v += t.popleft()

    return u, v


def solution(p):
    answer = ''
    if not p:  # empty
        return answer

    u, v = divde(p)

    if check(u):
        return u + solution(v)
    else:
        tmp = list(u)
        a = tmp[0]
        tmp[0] = tmp[-1]
        tmp[-1] = a
        print(tmp)
        u = ''.join(tmp)

        return '(' + solution(v) + ')' + u

    return answer


solution(s)