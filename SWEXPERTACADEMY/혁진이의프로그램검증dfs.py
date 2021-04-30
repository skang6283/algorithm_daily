import sys
sys.setrecursionlimit(100000)
T = int(input())

# > < ^ v
dx=[1,-1,0,0]
dy=[0,0,-1,1]
R,C=0,0
hk=[]

def go(visited,mem,dir,cy,cx):
    cur = hk[cy][cx]

    while cur != '@':
        if cur == '>':
            dir = 0
        elif cur == '<':
            dir = 1
        elif cur == '^':
            dir = 2
        elif cur == 'v':
            dir = 3
        elif cur == '_':
            if mem == 0:
                dir = 0
            else:
                dir = 1

        elif cur == '|':
            if mem == 0:
                dir = 3
            else:
                dir = 2

        elif cur == '?':
            if (cy, cx, mem, dir) in visited:
                return False
            else:
                visited.add((cy, cx, mem, dir))

            if go(visited, mem, 0,(cy + dy[0]) % R,(cx + dx[0]) % C):
                return True
            if go(visited, mem, 1,(cy + dy[1]) % R,(cx + dx[1]) % C):
                return True
            if go(visited, mem, 2,(cy + dy[2]) % R,(cx + dx[2]) % C):
                return True
            if go(visited, mem, 3,(cy + dy[3]) % R,(cx + dx[3]) % C):
                return True

        elif cur == '+':
            mem = (mem + 1) % 16
        elif cur == '-':
            mem = (mem - 1) % 16
        elif cur !='.':
            mem = int(cur)


        if (cy,cx,mem,dir) in visited:
            return False
        else:
            visited.add((cy,cx,mem,dir))


        cy = (cy + dy[dir]) % R
        cx = (cx + dx[dir]) % C
        cur = hk[cy][cx]

    return True


for test_case in range(1, T + 1):
    R,C = map(int,input().split())
    hk=[]
    for _ in range(R):
        hk.append(input())
    print(hk)
    print("cur,cy,cx,mem,dir")

    flag=0
    for row in hk:
        for letter in row:
            if letter =='@':
                flag=1
                break
        if flag:
            break

    if not flag:
        print("#"+str(test_case)+" NO")
        continue

    if go(set(), 0,0,0,0):
        print("#"+str(test_case)+" YES")
    else:
        print("#"+str(test_case)+" NO")




