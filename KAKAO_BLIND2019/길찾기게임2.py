import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,num):
        self.left = None
        self.right = None
        self.num = num

    def __str__(self):
        return "\n --%s %s %s" % (self.num, self.left, self.right)

def tree(nodeinfo,start,end):
    cur_index,high=0,0
    high=-1

    if start >=end:
        return
    for i in range(start,end):
        x,y,num = nodeinfo[i]
        print(x,y)
        if y > high:
            high = y
            cur_index = i

    node = Node(nodeinfo[cur_index][2])
    node.left = tree(nodeinfo,start,cur_index)
    node.right = tree(nodeinfo,cur_index+1,end)

    return node


def preorder(node,tmp):
    if node !=None:
        tmp.append(node.num)
        preorder(node.left,tmp)
        preorder(node.right,tmp)

    return tmp

def postorder(node,tmp):
    if node!=None:
        postorder(node.left,tmp)
        postorder(node.right,tmp)
        tmp.append(node.num)

    return tmp


def solution(nodeinfo):
    answer=[]
    if len(nodeinfo) == 1:
        answer.append([1])
        answer.append([1])
        return answer

    for i in range(len(nodeinfo)):
        y=nodeinfo[1]
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x:x[0])    # x,y,num
    print(nodeinfo)
    start,end=0,len(nodeinfo)
    root = tree(nodeinfo,start,end)
    answer.append(preorder(root,[]))
    answer.append(postorder(root,[]))

    print(answer)
    return answer

a = [[2,4]]
solution(a)