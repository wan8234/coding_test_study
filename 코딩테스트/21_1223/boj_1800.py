import sys
import heapq


input = sys.stdin.readline

INF = int(1e9)


N,P,K = map(int,input().split())

graph = [[] for _ in range(N + 1)]


for _ in range(P):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def dijkstra(start, cost_limit):

    q = []
    heapq.heappush(q, (0, start))  

    distance = [INF] * (N + 1)
    distance[start] = 0

    while q:
        cost, index = heapq.heappop(q)

        if distance[index] < cost:
            continue

        for i in graph[index]:

            if i[0] > cost_limit:
                if cost + 1 < distance[i[1]]:
                    distance[i[1]] = cost + 1
                    heapq.heappush(q, (cost + 1, i[1]))
            else:
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))

    if distance[N] > K:
        return False
        
    else:
        return True


left, right = 0, 1000001
answer = INF

while left <= right:

    mid = (left + right) // 2

    if dijkstra(1, mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

if answer != INF:
    print(answer)
else:
    print(-1)