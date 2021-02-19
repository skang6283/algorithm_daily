from collections import deque


# left 0 right 1
def dfs(input, dir, answer, n):
    ud = deque(input)
    if not ud:
        return answer

    if dir == 0:
        cur = ud.popleft()
        if not ud: return answer
        right = ud[0]
        left = ud[-1]

        answer = min(dfs(list(ud)[:], 0, answer + right - cur, n), dfs(list(ud)[:], 1, answer + n - left + cur, n))

    else:
        cur = ud.pop()
        if not ud: return answer

        right = ud[0]
        left = ud[-1]

        answer = min(dfs(list(ud)[:], 0, answer + cur - left, n), dfs(list(ud)[:], 1, answer + n - cur + right, n))

    return answer


def solution(name):
    answer = 0
    n = len(name)
    for letter in name:
        q, r = divmod((ord(letter) - ord('A')), 13)
        if q == 1:
            if r == 0:
                answer += 13
            else:
                answer += 13 - r
        else:
            answer += r

    ud = []
    for idx, letter in enumerate(name):
        if idx == 0:
            ud.append(0)
        elif letter != 'A':
            ud.append(idx)

    answer = dfs(ud, 0, answer, n)

    return answer