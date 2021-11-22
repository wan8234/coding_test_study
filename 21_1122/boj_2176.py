import sys
import heapq

input = sys.stdin.readline

def dijkstra(q,start):

    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for nval, nxt in graph[now]:
            nval += dist
            if distance[nxt] > nval:
                distance[nxt] = nval
                heapq.heappush(q, (nval, nxt))

def memo(a):

    if dp[a] != -1:
        return dp[a]

    if a == 2:
        return 1

    dp[a] = 0

    for nval, nxt in graph[a]:
        if distance[a] > distance[nxt]: #다음 정점에 대한 탐색을 완료, 다음 정점에 대해 구해놓은 거리보다 현재 정점까지의 거리가 더 큰 경우
            dp[a] += memo(nxt)
            
    return dp[a]

n,m = map(int,input().split())
S,T = 1,2

INF = int(1e9)

graph = [[] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)
distance[2] = 0
dp = [-1] * (n+1)
dp[2] = 1
q = list()

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dijkstra(q,T)

print(memo(S))

