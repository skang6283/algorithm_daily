T = int(input())

winO, winX = 'O won', 'X won'
incomplete = 'Game has not completed'
draw = 'Draw'


def check(row):
    t_cnt = 0
    cur = ''
    dr=0
    for t in row:
        if t !='T' and t != '.':
            cur = t
            break

    for t in row:
        if t == '.':
            return incomplete

        if t == 'T':
            t_cnt += 1
            continue

        if t != cur:
            dr=1
            continue

    ans='draw'
    if t_cnt >=2 or dr:
        ans=draw
    elif cur == 'O':
        ans = winO
    elif cur =='X':
        ans=winX

    return ans


for test_case in range(1, T + 1):

    board = [input().rstrip('\n') for _ in range(4)]
    flag = 0

    rows = []

    rows.extend(board)
    for x in zip(*board):
        rows.append("".join(list(x)))

    rows.append("".join([board[i][i] for i in range(len(board))]))
    rows.append("".join([board[i - 1][-i] for i in range(1, len(board) + 1)]))
    flag = 0

    for row in rows:
        res = check(row)
        if res == winO or res == winX:
            print("#" + str(test_case) + " " + res)
            break
        elif res == incomplete:
            flag = 1
    else:
        if not flag:
            print("#" + str(test_case) + " " + draw)
        else:
            print("#" + str(test_case) + " " + incomplete)

    if test_case != T:
        empty = input()