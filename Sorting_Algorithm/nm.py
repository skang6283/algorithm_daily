from itertools import permutations, combinations

# permutation : order does matter
# combination : order does not matter

def nm(n,d,m):
    if len(d)==m:
        print(*d)
        return

    for i in range(1,n+1):
        if i in d:
            continue
        d.append(i)
        nm(n,d,m)
        d.pop()

# n,m = map(int,input().split())
# arr=[i for i in range(1,n+1)]
# result=list(permutations(arr,m))
# for i in result:
#     print(*i)

def nm2(s,n,d,m):
    if len(d)==m:
        print(*d)
        return

    for i in range(s,n+1):
        if i in d:
            continue
        d.append(i)
        nm2(i,n,d,m)
        d.pop()

# n,m = map(int,input().split())
# arr=[i for i in range(1,n+1)]
# result=list(combinations(arr,m))
# for i in result:
#     print(*i)

def nm3(n,d,m):
    if len(d)==m:
        print(*d)
        return

    for i in range(1,n+1):

        d.append(i)
        nm3(n,d,m)
        d.pop()

def nm4(s,n,d,m):
    if len(d)==m:
        print(*d)
        return
    for i in range(s,n+1):

        d.append(i)
        nm4(i,n,d,m)
        d.pop()

if __name__ == "__main__":
    n,m = map(int, input().split())

    d =[]
    #nm(n,d,m)
    nm4(1,n,d,m)





