import sys
import math
input =sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

ans =0
for num in A:
    if num:
        num -=B
        ans+=1
    if num>0:
        ans += math.ceil(num/C)


print(ans)