import sys
input = sys.stdin.readline
from collections import deque

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    matrix = []
    for _ in range(n):
        line = list(map(int, input().split()))
        matrix.append(line)

    result = [[1e9] * n for _ in range(n)]

    dq = [(0, 0)]
    dq = deque(dq)
    result[0][0] = matrix[0][0]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                #nx, ny 값이랑 x, y 지나왔을 때 값 비교
                if result[nx][ny] > matrix[nx][ny] + result[x][y]:
                    result[nx][ny] = matrix[nx][ny] + result[x][y]
                    dq.append((nx, ny))

    print("Problem ", cnt, ": ", result[-1][-1], sep="")
    cnt += 1

