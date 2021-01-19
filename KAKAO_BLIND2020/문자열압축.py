import sys

s= input()


def solution(s):
    answer = len(s)
    cur = []

    for length in range(1, len(s) // 2 + 1):
        cur = s[:length]
        cnt = 1
        tmp = ""
        for i in range(length, len(s), length):

            if cur == s[i:i + length]:
                cnt += 1
            elif cur != s[i:i + length]:

                if cnt == 1:
                    tmp+=cur
                else:
                    tmp += str(cnt) + cur
                    cnt=1

                cur = s[i:i + length]
        if cnt == 1:
            tmp += cur
        else:
            tmp += str(cnt) + cur
            cnt = 1

        cur = s[i:i + length]
        answer = min(answer, len(tmp))
    return answer

print(solution(s))
