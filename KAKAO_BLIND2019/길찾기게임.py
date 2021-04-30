from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

levelx,levely=defaultdict(int),defaultdict(list)

def findl(nodeinfo,parent,minx):
    maxx,cy=nodeinfo[parent][0],nodeinfo[parent][1]

    left=-1
    lefty=0
    leftx=0
    for level,num in levelx.items():
        x,y = nodeinfo[num]
        if x > minx and x < maxx and y < cy:
            if y >lefty:
                left = num
                lefty=y
                leftx=x

    return left,maxx


def findr(nodeinfo,parent,maxx):
    minx,cy=nodeinfo[parent][0],nodeinfo[parent][1]

    righty=0
    rightx=0
    right = -1
    for level, num in levelx.items():
        x, y = nodeinfo[num]
        if x > minx and x < maxx and y < cy:
            if y > righty:
                right = num
                righty = y
                rightx = x
    return right,minx


def preorder(nodeinfo,node,minx,maxx,ans):

    left,new_maxx = findl(nodeinfo,node,minx)
    if left != -1:
        ans.append(left)
        preorder(nodeinfo,left,minx,new_maxx,ans)



    right,new_minxx = findr(nodeinfo,node,maxx)
    if right !=-1:
        ans.append(right)
        preorder(nodeinfo,right,new_minxx,maxx,ans)


def postorder(nodeinfo,node,minx,maxx,ans):

    left, new_maxx = findl(nodeinfo, node, minx)
    if left != -1:
        postorder(nodeinfo, left, minx, new_maxx, ans)
        ans.append(left)

    right, new_minxx = findr(nodeinfo, node, maxx)
    if right != -1:
        postorder(nodeinfo, right, new_minxx, maxx, ans)
        ans.append(right)


def solution(nodeinfo):
    global levelx,levely
    root,rooty,bigx = 0,0,0

    answer=[]
    for num, node in enumerate(nodeinfo):

        levelx[node[0]] = num
        levely[node[1]].append(num)
        if node[1]>rooty:
            root = num
            rooty = node[1]
        if node[0] > bigx:
            bigx=node[0]

    tmp=[]
    tmp.append(root)
    preorder(nodeinfo,root,0,bigx+1,tmp)
    tmp = [num+1 for num in tmp]
    answer.append(tmp)


    tmp = []
    postorder(nodeinfo, root, 0, bigx + 1, tmp)
    tmp.append(root)
    tmp = [num+1 for num in tmp]
    answer.append(tmp)

    return answer
a = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(a)