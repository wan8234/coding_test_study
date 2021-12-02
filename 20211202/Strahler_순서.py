import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    K, M, P = map(int, input().split())
    dic = dict()
    go = [0] * (M+1)
    S = [-1] * (M+1)
    dq = deque()

    for _ in range(P):
        x, y = map(int, input().split())
        if y in dic:
            dic[y].append(x)
        else:
            dic[y] = [x]
        go[x] += 1
        dq.append(y)


    cnt = 0
    while dq:
        cnt += 1
        x = dq.popleft()
        p = True
        #들어오는 강 없으면 1
        if x not in dic:
            S[x] = 1
        else:
            arr = []
            for i in dic[x]:
                if S[i] == -1:
                    #x에 들어오는 강에 대한 순서가 아직 정해지지 않았음
                    #들어오는 강에 대한 것부터 찾기 - i 대기열에 넣기
                    dq.append(i)
                    p = False
                else:
                    #들어오는 강 순서
                    arr.append(S[i])
            if p:
                maxi = max(arr)
                #x의 순서 정하기
                if arr.count(maxi) >= 2:
                    S[x] = maxi + 1
                else:
                    S[x] = maxi
            else:
                #아직 정해지지 않았으면 x 다시 넣기
                dq.append(x)
        
    #go가 0이면 나가는 물이 없는 것 == 바다와 통하는 곳
    go[0] = -1
    print(K, S[go.index(0)])