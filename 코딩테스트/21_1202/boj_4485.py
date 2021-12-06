import sys
from collections import deque

input = sys.stdin.readline

cnt = 0
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, graph, costs):

    queue = deque()
    queue.append((i, j))

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] > costs[x][y] + graph[nx][ny]:

                    costs[nx][ny] = costs[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

while True:

    n = int(input())


    if n == 0:
        break

    else:
        cave = [list(map(int,input().split())) for _ in range(n)]
        cost = [[INF] * n for _ in range(n)]

        cost[0][0] = cave[0][0]

        bfs(0, 0, cave, cost)

        answer = cost[n-1][n-1]

        cnt += 1
        print('Problem {0}: {1}'.format(cnt,answer))