from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

R, C = map(int, input().split())
start = []
goal = []
water = deque()
board = []
visit = [[0] * C for _ in range(R)]
water_visit = [[0] * C for _ in range(R)]

for i in range(R):
    line = list(input().rstrip())
    for j in range(C):
        if line[j] == 'S':
            start = [i, j, 0]
            visit[i][j] = 1
            line[j] = '.'
        elif line[j] == 'D':
            goal = [i, j]
        elif line[j] == '*':
            water.append([i, j, 0])
            water_visit[i][j] = 1
    board.append(line)

def bfs():
    queue = deque()
    queue.append(start)
    while queue or water:
        if water:
            tx, ty, t_flag = water[0]
            while water:
                if t_flag == water[0][2]:
                    wx, wy, w_flag = water.popleft()
                    for i in range(4):
                        nx, ny = wx + dx[i], wy + dy[i]
                        if 0 <= nx < R and 0 <= ny < C and water_visit[nx][ny] == 0 and board[nx][ny] == '.':
                            water_visit[nx][ny] = 1
                            water.append([nx, ny, w_flag + 1])
                else:
                    break
        
        if queue:
            cx, cy, c_flag = queue[0]
            while queue:
                if c_flag == queue[0][2]:
                    x, y, cnt = queue.popleft()
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == 0 and water_visit[nx][ny] == 0:
                            if board[nx][ny] == '.':
                                visit[nx][ny] = 1
                                queue.append([nx, ny, cnt + 1])
                            elif board[nx][ny] == 'D':
                                return cnt + 1
                else:
                    break

result = bfs()

print(result if result else 'KAKTUS')
