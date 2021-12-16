import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
matrix = []
S = 0
for i in range(n):
    line = list(input().strip('\n'))
    for j in range(m):
        if line[j] == 'S':
            S = (i, j)
            line[j] = "."
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def water():
    arr = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == "*":
                        arr.append((i, j))
                        break
    for x, y in arr:
        matrix[x][y] = '*'

dq = [(S[0], S[1], 0)]
dq = deque(dq)
cnt = 0
visited = [[0] * m for _ in range(n)]

water()
while dq:
    x, y, c = dq.popleft()
    if matrix[x][y] == 'D':
        print(c)
        break
    if c > cnt:
        water()
        cnt = c
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if matrix[nx][ny] == "." or matrix[nx][ny] == "D":
                dq.append((nx, ny, c + 1))
                visited[nx][ny] = 1
else:
    print("KAKTUS")
