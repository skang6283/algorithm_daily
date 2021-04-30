
T = int(input())
for test_case in range(1, T + 1):
    D,N = map(int,input().split())
    horse=[]

    for _ in range(N):
        horse.append(map(int,input().split()))  #K,S

    time=[]
    for K,S in horse:
        t = (D-K)/S
        time.append(t)

    ans = D/max(time)

    print("#"+str(test_case)+" "+str(format(ans,'.7f')))