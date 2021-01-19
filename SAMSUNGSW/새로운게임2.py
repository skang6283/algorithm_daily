import sys

input = sys.stdin.readline

N,K = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
# 0 - white, 1 - red, 2 - blue

piece=[]
pieceloc=[[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    r,c,d = map(int,input().split())
    piece.append([r-1,c-1,d-1])
    pieceloc[r-1][c-1].append(i)
dy=[0,0,-1,1]
dx=[1,-1,0,0]
# 0,1,2,3

def pb():
    for a in pieceloc:
        print(a)



cnt=0
flag=0
def turn(i,bcnt):
    cy,cx,d = piece[i]

    #print(i,cy,cx,d)
    #print(i,cy,cx,t)
    stack=[]


    cur = pieceloc[cy][cx].pop()
    stack.append(cur)
    while True:
        if cur == i:
            break
        cur = pieceloc[cy][cx].pop()
        stack.append(cur)

    ny,nx = cy+dy[d],cx+dx[d]
    #blue
    print(stack)
    if ny<0 or nx<0 or ny>=N or nx>=N or board[ny][nx]==2:
        print("blue")
        stack.reverse()
        if bcnt:
            pieceloc[cy][cx].extend(stack)
            return
        if d ==0 or d ==2:
            d+=1
        else:
            d-=1
        pieceloc[cy][cx].extend(stack)
        piece[i][2]=d
        turn(i,1)


    #red
    elif board[ny][nx]==1:
        print("red")

        pieceloc[ny][nx].extend(stack)
        print(stack)
        print(pieceloc[ny][nx])

        for member in stack:
            piece[member][0],piece[member][1]=ny,nx

        if len(pieceloc[ny][nx]) >= 4:
            return 1

    #white
    elif board[ny][nx] == 0:
        print("white")
        stack.reverse()
        pieceloc[ny][nx].extend(stack)

        for member in stack:
            piece[member][0],piece[member][1]= ny,nx

        if len(pieceloc[ny][nx]) >= 4:
            return 1



def pb():
    for a in pieceloc:
        print(a)
    print()
def pl():
    for a in piece:
        print(a)

flag=0
while True:
    if cnt >1000:
        cnt=-1
        break
    if flag:
        break
    cnt+=1


    for i in range(K):
        if turn(i,0):
            flag=1
            break
        pb()
    print("------------")



print(cnt)