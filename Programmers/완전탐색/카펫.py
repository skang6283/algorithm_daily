
def solution(brown, yellow):
    answer = []

    total  = int((brown+4) / 2)
    for x in range(int(total/2)+1):
        y = total-x

        if (x-2)*(y-2) == yellow:
            answer=[y,x]
            break


    return answer
