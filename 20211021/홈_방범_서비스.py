from collections import deque

t = int(input())
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
cost = [k * k + (k - 1) * (k - 1) for k in range(24)]


def bfs(x, y):
    global maxCnt
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    q = deque([(x, y)])

    home = arr[x][y]
    size = 1

    if home * m - cost[size] >= 0:
        maxCnt = max(home, maxCnt)

    while size <= n+1:
        for i in range(len(q)):
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

                    if arr[nx][ny] != 0:
                        home += 1

        if home * m - cost[size + 1] >= 0:
            maxCnt = max(home, maxCnt)
        size += 1


for case in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxCnt = 0
    for i in range(n):
        for j in range(n):
            bfs(i, j)       # 모든 위치에서 검사
    print(f"#{case+1} {maxCnt}")
