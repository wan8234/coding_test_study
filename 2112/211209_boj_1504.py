import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

N, E = map(int, input().split())
route = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    route[a].append([b, c])
    route[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    dp = [inf for _ in range(N + 1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        weight, node = heapq.heappop(heap)

        for next_node, next_weight in route[node]:
            new_weight = next_weight + weight

            if dp[next_node] > new_weight:
                dp[next_node] = new_weight
                heapq.heappush(heap, [new_weight, next_node])
    
    return dp

node_first = dijkstra(1)
node_v1 = dijkstra(v1)
node_v2 = dijkstra(v2)
result = min(node_first[v1] + node_v1[v2] + node_v2[N], node_first[v2] + node_v2[v1] + node_v1[N])

print(result if result < inf else -1)
