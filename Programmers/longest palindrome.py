def checkFromMid(idx, s):
    # start empty abba
    case1 = 0
    left = idx;
    right = idx + 1
    while (left >= 0 and right <= (len(s) - 1)):
        if s[left] == s[right]:
            case1 += 2
        else:
            break
        left -= 1;
        right += 1

    case2 = 1
    left = idx - 1;
    right = idx + 1
    while (left >= 0 and right <= (len(s) - 1)):
        if s[left] == s[right]:
            case2 += 2
        else:
            break
        left -= 1;
        right += 1
        # start letter

    return max(case1, case2)


def solution(s):
    answer = 0

    for idx in range(len(s)):
        answer = max(answer, checkFromMid(idx, s))

    return answer