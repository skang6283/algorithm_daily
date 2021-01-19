from itertools import permutations,combinations

def dfs(depth, rst, add,sub,mul,div):
    if depth == n:
        output.append(rst)
        return

    if add:
        dfs(depth+1,rst + nums[depth],add-1,sub,mul,div)
    if sub:
        dfs(depth+1,rst - nums[depth],add,sub-1,mul,div)
    if mul:
        dfs(depth+1,rst * nums[depth],add,sub,mul-1,div)
    if div:
        dfs(depth+1,int(rst / nums[depth]),add,sub,mul,div-1)

n = int(input())
nums = [int(x) for x in input().split()]
add,sub,mul,div = [int(x) for x in input().split()] # 0+,1-,2x,3%


output =list()

if __name__=="__main__":
    dfs(1,nums[0],add,sub,mul,div)

    print(max(output))
    print(min(output))