def solution(n):
    answer = []
    triangle = [[0] * n for _ in range(n)]

    cnt = 1

    d_col = 0
    d_start = 0

    r_row = n - 1
    r_start = 1

    u_col = n - 1
    u_start = n - 2
    while n >= 0:
        print(n)
        # down
        for i in range(d_start, d_start + n, 1):
            triangle[i][d_col] = cnt
            cnt += 1;
        n -= 1
        d_col += 1
        d_start += 2

        # right
        for i in range(r_start, r_start + n, 1):
            triangle[r_row][i] = cnt
            cnt += 1
        n -= 1
        r_row -= 1
        r_start += 1

        # up
        for i in range(u_start, u_start - n, -1):
            triangle[i][u_col] = cnt
            cnt += 1
        n -= 1
        u_col -= 1
        u_start -= 1

    for a in triangle:
        for num in a:
            if num != 0:
                answer.append(num)

    return answer


# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# 6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
