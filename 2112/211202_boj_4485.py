from heapq import heappush, heappop
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

inf = int(1e9)
test_case = 1

def dijkstra():
    distance = [[inf] * N for _ in range(N)]

    queue = []
    heappush(queue, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while queue:
        cost, x, y = heappop(queue)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + graph[nx][ny]

                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heappush(queue, (new_cost, nx, ny))

    return distance[N - 1][N - 1]


while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra()

    print('Problem {}: {}'.format(test_case, result))
    test_case += 1
