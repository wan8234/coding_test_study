import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, depth, total):
    global max_value
    if total + maxi * (4 - depth) <= max_value:
        return
    if depth >= 4:
        max_value = max(max_value, total)
        return
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                if depth == 2:
                    visit[nx][ny] = 1
                    dfs(x, y, depth + 1, total + board[nx][ny])
                    visit[nx][ny] = 0
                
                visit[nx][ny] = 1
                dfs(nx, ny, depth + 1, total + board[nx][ny])
                visit[nx][ny] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

maxi = max(map(max, board))

max_value = 0
visit = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visit[i][j] = 0

print(max_value)    