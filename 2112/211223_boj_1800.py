import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

N, P, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(P):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start, cut):
    heap = []
    distance = [inf] * (N + 1)
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if distance[node] < cost:
            continue

        for next_node in graph[node]:
            if next_node[0] > cut:
                if cost + 1 < distance[next_node[1]]:
                    distance[next_node[1]] = cost + 1
                    heapq.heappush(heap, (cost + 1, next_node[1]))
        
            else:
                if cost < distance[next_node[1]]:
                    distance[next_node[1]] = cost
                    heapq.heappush(heap, (cost, next_node[1]))
    
    if distance[N] > K:
        return False
    else:
        return True

left, right = 0, inf
answer = inf

while left <= right:
    mid = (left + right) // 2
    result = dijkstra(1, mid)
    if result:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer if answer != inf else -1)