from itertools import permutations,combinations


def calc(start,link):
    startsum = 0
    linksum = 0

    for i in start:
        for j in start:
            startsum += stat[i-1][j-1]

    for i in link:
        for j in link:
            linksum += stat[i-1][j-1]

    return abs(startsum-linksum)

n = int(input())
stat=[]
member =[]
mindiff = 1000000000
for i in range(n):
    member.append(i+1)
    stat.append([int(x) for x in input().split()])

check = list(combinations(member,n//2))

for i in range(len(check)//2):
    a= calc(check[i],check[-1-i])
    if a < mindiff:
        mindiff=a
print(mindiff)

