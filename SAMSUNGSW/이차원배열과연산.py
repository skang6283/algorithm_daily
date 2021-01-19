import sys

def printA():
    for i in range(10):
        print(A[i][0:10])
    print()

input = sys.stdin.readline

r,c,k = map(int,input().split())
A =[[0]*101 for _ in range(101)]
for i in range(3):
    A[i][0],A[i][1],A[i][2]= map(int,input().split())

cnum=3
rnum=3

def calc_r(row):
    global rnum
    tmp = [0] * 101
    h = []
    nums =[]

    for i in range(cnum):

        idx = A[row][i]
        if idx==0: continue
        A[row][i]=0
        tmp[idx] += 1
        if idx not in nums:
            nums.append(idx)


    for num in nums:
        h.append((tmp[num],num))
    h.sort(reverse=True)

    index = 0
    for index in range(len(h)):
        cnt,num = h.pop()
        if index >=50:
            break

        A[row][index*2] = num
        A[row][index * 2+1] = cnt

    return index*2+2


def calc_c(col):
    tmp = [0] * 101
    h = []
    nums = []

    for i in range(rnum):
        idx = A[i][col]
        if idx==0: continue
        A[i][col] = 0
        tmp[idx] += 1
        if idx not in nums:
            nums.append(idx)

    for num in nums:
        h.append((tmp[num], num))
    h.sort(reverse=True)
    index = 0
    for index in range(len(h)):

        cnt,num = h.pop()
        if index >= 50:
            break
        A[index * 2][col] = num
        A[index * 2 + 1][col] = cnt

    return index*2+2

cnt =0
while A[r-1][c-1] != k:
    if cnt >=100:
        cnt=-1
        break
    cnt+=1

    if rnum >= cnum:
        cnum_list=[]
        for i in range(rnum):
            cnum_list.append(calc_r(i))
        cnum = max(cnum_list)
    else:
        rnum_list=[]
        for i in range(cnum):
            rnum_list.append(calc_c(i))
        rnum = max(rnum_list)

print(cnt)