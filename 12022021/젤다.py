import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1

def dijkstra():
    q = []
    # 도둑루피 값, x, y
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                cost_new = cost + graph[nx][ny]
                if cost_new < distance[nx][ny]:
                    distance[nx][ny] = cost_new
                    heapq.heappush(q, (cost_new, nx, ny))

while True:
    n = int(input())
    if n == 0:
        break
    graph = [ list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] *n for _ in range(n)]

    dijkstra()
    cnt += 1
