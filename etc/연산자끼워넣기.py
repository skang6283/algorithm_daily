from itertools import permutations,combinations
n = int(input())
nums = [int(x) for x in input().split()]
tmp = [int(x) for x in input().split()] # 0+,1-,2x,3%
ops=[]
for i in range(4):
    for j in range(tmp[i]):
        ops.append(i)

ops = list(set(permutations(ops)))
max= -1000000000
min = 1000000000

def calc(op,a,b):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    return int(a/b)

def go(op):
    a = nums[0]
    global max,min
    for i in range(n-1):
        a = calc(op[i],a,nums[i+1])
    if a > max:
        max = a
    if a < min:
        min = a



if __name__=="__main__":

    for op in ops:
        go(op)

    print(max)
    print(min)

