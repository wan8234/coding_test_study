from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        a, b = map(int, input().split())
        in_degree[b] += 1
        tree[a].append(b)
    queue = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = cost[i]
    
    while queue:
        current = queue.popleft()
        for i in tree[current]:
            in_degree[i] -= 1
            dp[i] = max(dp[current] + cost[i], dp[i])
            if in_degree[i] == 0:
                queue.append(i)
    
    W = int(input())

    print(dp[W])

#### TRY BFS (FAIL) ####
# T = int(input())

# for test_case in range(T):
#     N, K = map(int, input().split())
#     flag = [0] * (N + 1) # build 여부
#     build_time = [0]
#     build_time.extend(list(map(int, input().split())))

#     past_build = {} # 이전에 지어야 하는 건물
#     future_build = {} # 이후에 지을 수 있는 건물

#     for i in range(K):
#         first, second = map(int, input().split())

#         if first in future_build:
#             future_build[first].append(second)
#         else:
#             future_build[first] = [second]
        
#         if second in past_build:
#             past_build[second].append(first)
#         else:
#             past_build[second] = [first]
    
#     W = int(input())

#     queue = deque()
#     queue.append(W)

#     time = 0

#     while queue:
#         current = queue.popleft()

     
