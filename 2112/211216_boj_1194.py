from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
queue = deque()
visit = [[[0] * 64 for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    row = list(input().rstrip())
    board.append(row)
    for j in range(M):
        if row[j] == '0':
            queue.append([i, j, 0, 0])
            board[i][j] = '.'
            visit[i][j][0] = 1

def bfs():
    while queue:
        x, y, key, count = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and visit[nx][ny][key] == 0:
                if board[nx][ny] == '1':
                    return count + 1
                elif board[nx][ny] == '.':
                    visit[nx][ny][key] = 1
                    queue.append([nx, ny, key, count + 1])
                else:
                    if ord('A') <= ord(board[nx][ny]) <= ord('Z'):
                        if key & (1 << (ord(board[nx][ny]) - ord('A'))):
                            visit[nx][ny][key] = 1
                            queue.append([nx, ny, key, count + 1])
                    elif ord('a') <= ord(board[nx][ny]) <= ord('z'):
                        solve = key | (1 << (ord(board[nx][ny]) - ord('a')))                        
                        if visit[nx][ny][solve] == 0:
                            visit[nx][ny][solve] = 1
                            queue.append([nx, ny, solve, count + 1])
    return -1

print(bfs())