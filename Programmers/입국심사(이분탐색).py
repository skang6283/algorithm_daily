def solution(n, times):
    answer = 0

    left = min(times) * n // len(times)
    right = max(times) * n // len(times)

    while left < right:
        mid = (left + right) // 2
        tmp = 0
        for t in times:
            tmp += mid // t

        if tmp >= n:
            right = mid
        else:
            left = mid + 1

    return left