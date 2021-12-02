import sys
input = sys.stdin.readline

N, M = map(int, input().split())
higher_rankers = [set() for _ in range(N+1)]
lower_rankers = [set() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    higher_rankers[a].add(b)
    lower_rankers[b].add(a)

for i in range(N+1):
    # i < higher_ranker -> i보다 작은사람은 higher보다 작음
    for higher_ranker in higher_rankers[i]:
        lower_rankers[higher_ranker].update(lower_rankers[i])
    # i > lower_ranker -> i보다 큰 사람은 lower보다 큼
    for lower_ranker in lower_rankers[i]:
        higher_rankers[lower_ranker].update(higher_rankers[i])

#res = sum(1 for i in range(N+1) if len(higher_rankers[i]) + len(lower_rankers[i]) == N - 1)
res = 0
for i in range(N+1):
    if len(higher_rankers[i]) + len(lower_rankers[i]) == N - 1:
        res += 1
print(res)


# pypy3이용
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] *(N+1) for _ in range(N+1)]

for _ in range(M):
    s, t = map(int, input().split())
    graph[s][t] = 1

# 플로이드 워셜
for k in range(1, N+1): 
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1 #자신보다 작은 경우


res = 0
for i in range(1, N+1):
    total = 1
    for j in range(1, N+1):
        # 누가 큰지 알면 1
        total += graph[i][j] + graph[j][i]
    # N명의 순서를 알경우
    if total == N: 
        res += 1
print(res)
'''
