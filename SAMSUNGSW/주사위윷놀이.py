import sys

input = sys.stdin.readline
dice = list(map(int,input().split()))

board = [0]*100
for i in range(21):
    board[i] = i*2

#[1, 1, 1, 2, 3, 3, 3, 3, 3, 1]
#5 1 2 3 4 5 5 3 2 4

board[31],board[32],board[33] = 13,16,19
board[51],board[52],board[53] = 28,27,26
board[71],board[72],board[73],board[74],board[75]= 22,24,25,30,35


most=0

horse = [0]*4
visited = set()

def move(start,dist):
    if start == 5 : start = 30
    elif start == 10 : start = 70
    elif start == 15 : start = 50

    if 30 <= start and start <=60:                # go to25
        while dist:
            start +=1
            dist  -=1
            if start <= 70 and start%10 == 4:
                start = 73
    if start+dist == 76 :
        return 20

    return start+dist


def dfs(index,sum):
    global most

    if index == 10:
        most = max(sum,most)
        return

    for i in range(4):
        if board[horse[i]] == 0 and horse[i] != 0: continue           # reached the end

        nxt = move(horse[i],dice[index])

        if nxt in horse and board[nxt] != 0:
            continue           # 도착지점에 이미 존재

        tmp = horse[i]
        horse[i] = nxt
        check = horse[:]                    # check visited
        #if tuple(check) in visited:
        #    horse[i] = tmp
        #    continue


        #visited.add(tuple(check))
        dfs(index+1,sum+board[nxt])
        horse[i] = tmp


dfs(0,0)
print(most)