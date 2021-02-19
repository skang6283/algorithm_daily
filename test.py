def inside(x1,y1,x2,y2,px1,py1,px2,py2):
    if x2 > px1 and px2 > x1 and y2 > py1 and py2 > y1: return True
    return False

def inside(x,y,px1,py1,px2,py2):
    if x >px1 and x<px2 and y > py1 and y<py2:
        return True

def solution(boxes):
    dist = 100000000
    answer=[]
    present =[]
    index=0
    for x1,y1,x2,y2 in boxes:
        x1+=dist;y1+=dist;x2+=dist;y2+=dist;

        if index == 0:
            answer.append(index)
            present.append([x1,y1,x2,y2])
        else:
            for px1,py1,px2,py2 in present:
                if inside(x1,y1,x2,y2,px1,py1,px2,py2) or inside(px1,py1,px2,py2,x1,y1,x2,y2):
                    break
            else:
                answer.append(index)
                present.append([x1,y1,x2,y2])

        index+=1

    return answer

boxes=[[1,1,3,3],[2,2,4,4],[1,6,5,7],[3,3,5,5]]
a = solution(boxes)

print(a)