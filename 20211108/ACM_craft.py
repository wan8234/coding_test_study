import sys
input = sys.stdin.readline

from collections import deque

T = int(input())


for _ in range(T):
    N, K = map(int, input().split())

    time = list(map(int, input().split()))
    time.insert(0, 0)

    dp = [0] * (N+1)

    connection = [[] for _ in range(N+1)]
    #먼저 건설해야하는 빌딩 수 저장
    seq = [0] * (N+1)

    for _ in range(K):
        x, y = map(int, input().split())
        #x를 지으면 y를 지을 수 있음
        connection[x].append(y)
        #y를 지으려면 seq[y]개의 건물을 지어야함
        seq[y] += 1

    dq = deque()

    #지금 지을 수 있는 건물
    for i in range(1, N+1):
        if seq[i] == 0:
            dq.append(i)

    while dq:
        x = dq.popleft()
        #x를 지으면 지을 수 있는 건물
        for y in connection[x]:
            #x를 지었으므로 지어야 하는 건물 -1
            seq[y] -= 1
            # 건물 시간 최대로
            dp[y] = max(dp[x] + time[x], dp[y])
            if seq[y] == 0:
                dq.append(y)
        

    W = int(input())
    print(dp[W] + time[W])
