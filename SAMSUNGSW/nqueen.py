yy=[]
board=[[]]
count=0

def check(y,x,n):
    if yy[x] == 1:
        return False

    for i,j in zip(range(y,-1,-1),range(x,-1,-1)):
        if board[i][j]==1:
            return False

    for i,j in zip(range(y,-1,-1),range(x,n,1)):
        if board[i][j]==1:
            return False
    return True

def nq(y,n):
    global count,yy,board
    if y == n:
        count += 1
        return

    for x in range(n):

        if check(y,x,n):
            board[y][x] =1
            yy[x] = 1
            nq(y+1,n)
            board[y][x]=0
            yy[x]=0

if __name__ =="__main__":
    n =int(input())

    yy = [0 for i in range(n)]
    board = [[0 for i in range(n)] for j in range(n)]
    nq(0,n)
    print(count)