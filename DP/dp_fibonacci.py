# 0,1,1,2,3,5,8,13,21

# 0 1 2 3 4 5 6
# 1 2 3 4 5 6 7,8,9

countzero=[1,0]
countone=[0,1]
def dp_fib(n):
    if n < len(countzero):
        return countzero[n],countone[n]

    for i in range(len(countzero),n+1):
        countzero.append(countzero[i-1]+ countzero[i-2])
        countone.append(countone[i-1] +countone[i-2])

    return countzero[n],countone[n]

if __name__=="__main__":
    t = int(input())
    tc = [int(input()) for i in range(t)]

    for i in tc:
        zero,one= dp_fib(i)
        print(zero,one)