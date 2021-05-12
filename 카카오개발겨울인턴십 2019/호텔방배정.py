from collections import defaultdict

def solution(k, room_number):
    answer = []
    next = {}

    for wanted in room_number:
        n = next.get(wanted, 0)
        if n:
            tmp = [n]
            while True:
                idx = n
                n = next.get(n,0)



        else:
            answer.append(n)
            next[n]=n+1

    return answer



a = solution(10,[1,3,4,1,3,1])  #[1,3,4,2,5,6]
print(a)