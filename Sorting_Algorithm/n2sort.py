def insertionSort(nlist):

    for i in range(len(nlist)):
        j=i
        while j > 0 and nlist[j-1]>nlist[j]:
            nlist = swap(nlist,j-1,j)
            j -=1
    return nlist

def bubbleSort(nlist):
    for i in range(1,len(nlist)):
        for j in range(len(nlist)-i):
            if nlist[j] > nlist[j+1]:
                swap(nlist,j,j+1)

def swap(list, pos1,pos2):
    list[pos1], list[pos2]= list[pos2], list[pos1]

if __name__ == '__main__':

    n = int(input());
    #nlist = [int(x) for x in input().split()]
    nlist = [int(input()) for i in range(n)]

    print("before sort:",nlist)
    bubbleSort(nlist)
    print("after sort:",nlist)
