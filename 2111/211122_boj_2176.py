import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inf = int(1e9)
distance = [inf] * 1001
dp = [0] * 1001

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance[2] = 0
dp[2] = 1

queue = []
heapq.heappush(queue, [0, 2])

while queue:
    length, node = heapq.heappop(queue)

    if length > distance[node]:
        continue

    for i in graph[node]:
        temp = i[1] + length

        if temp < distance[i[0]]:
            distance[i[0]] = temp
            heapq.heappush(queue, [temp, i[0]])

        if length > distance[i[0]]:
            dp[node] += dp[i[0]]
            
print(dp[1])