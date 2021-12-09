import sys
import heapq


input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n + 1)]

INF = float('inf')
start = 1

for _ in range(e):

    a,b,c = map(int,input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int,input().split())


def dijkstra(start, end):


    distance = [INF] * (n + 1)
    distance[start] = 0

    q = []

    heapq.heappush(q, (start, 0))
    

    while q:
        
        now, dist = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance[end]
            

route1 = dijkstra(start, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
route2 = dijkstra(start, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if route1 == INF and route2 == INF:
    print(-1)
else:
    print(min(route1,route2))

