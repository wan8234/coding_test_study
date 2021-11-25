from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
result = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global result
    queue = set([(x, y, board[x][y])])

    while queue:
        x, y, visit = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visit:
                queue.add((nx, ny, visit + board[nx][ny]))
                result = max(result, len(visit) + 1)

# def bfs(x, y):
#     global result
#     queue = deque()
#     queue.append([x, y, board[x][y]])

#     while queue:
#         x, y, visit = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visit:
#                 queue.append([nx, ny, visit + board[nx][ny]])
#                 result = max(result, len(visit) + 1)

bfs(0, 0)
print(result)