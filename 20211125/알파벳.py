import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

matrix = []
for _ in range(R):
    line = list(input().strip('\n'))
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
check = [0] * 26
visited = [[0] * C for _ in range(R)]
def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and check[ord(matrix[nx][ny]) - ord('A')] == 0:
            visited[nx][ny] = 1
            check[ord(matrix[nx][ny]) - ord('A')] += 1
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0
            check[ord(matrix[nx][ny]) - ord('A')] -= 1

        
check[ord(matrix[0][0]) - ord('A')] = 1
visited[0][0] = 1
dfs(0, 0, 1)
print(answer)