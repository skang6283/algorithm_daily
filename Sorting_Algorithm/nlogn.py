import heapq
import sys

####################################################################
def buildMaxHeap(n,arr):
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
    print(arr)

def heapify(arr,n,i):
    max = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[left] > arr[i]:
        max = left
    else:
        max = i

    if right<n and arr[right] > arr[max]:
        max = right

    if max != i:
        swap(arr,i,max)
        heapify(arr,n,max)

def heapsort(arr,n):
    for i in range(n-1,0,-1):
        swap(arr,0,i)
        heapify(arr,i,0)
####################################################################
def heapqsort(arr,n):
    maxheap = []
    for num in arr:
        heapq.heappush(maxheap,num)

    sorted_array =[]
    for i in range(n):
        sorted_array.append(heapq.heappop(maxheap))
    return sorted_array
####################################################################
def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n//2
    l = mergesort(arr[:mid])
    r = mergesort(arr[mid:])

    return merge(l,r)

def merge(L,R):
    sorted = []
    i=j=k=0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            sorted.append(L[i])
            i +=1
        else:
            sorted.append(R[j])
            j+=1

    while i < len(L):
        sorted.append(L[i])
        i+=1

    while j < len(R):
        sorted.append(R[j])
        j+=1

    return sorted
####################################################################
def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def easy():
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(sys.stdin.readline()))
    for i in sorted(l):
        sys.stdout.write(str(i)+'\n')


if __name__ == '__main__':
    n = int(input());
    #nlist = [int(x) for x in input().split()]
    nlist = [int(input()) for i in range(n)]

    print("before sort:",nlist)

    # no module
    # heapsort
    # buildMaxHeap(n,nlist)
    # print("after buildmaxHeap:",nlist)
    # heapsort(nlist,n)
    # print("after heapsort:",nlist)

    #using heapq
    #sorted_array = heapqsort(nlist,n)
    #print("using heapqsort:",sorted_array)

    #using mergesort
    nlist = mergesort(nlist)
    print("using mergesort:",nlist)
