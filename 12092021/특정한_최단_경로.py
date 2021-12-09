import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for i in range(N + 1)]
INF = sys.maxsize

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    dp = [INF for i in range(N + 1)]
    dp[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        w, c = heapq.heappop(q)
        for a, b in graph[c]:
            weight = b + w
            if dp[a] > weight:
                dp[a] = weight
                heapq.heappush(q, (weight, a))
    return dp

one = dijkstra(1)
r_v1 = dijkstra(v1)
r_v2 = dijkstra(v2)
cnt = min(one[v1] + r_v1[v2] + r_v2[N], one[v2] + r_v2[v1] + r_v1[N])
print(cnt if cnt < INF else -1)
