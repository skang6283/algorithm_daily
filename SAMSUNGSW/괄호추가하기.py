import sys
def calc(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    return num1*num2


def dfs(res,nums,ops,idx):
    global answer
    if idx >= len(nums)-1:
        if answer <= res:
            answer = res
        return

    res1 = calc(res,nums[idx+1],ops[idx])
    dfs(res1,nums,ops,idx+1)


    if (idx< len(nums)-2):
        tmp = calc(nums[idx+1],nums[idx+2],ops[idx+1])
        res2 = calc(res,tmp,ops[idx])
        dfs(res2,nums,ops,idx+2)



input = sys.stdin.readline
n,eq=input(),input()

answer= -1*sys.maxsize
nums=[]; ops=[]
for letter in eq:
    if letter.isnumeric():
        nums.append(int(letter))
    else:
        ops.append(letter)

dfs(nums[0],nums,ops,0)

print(answer)