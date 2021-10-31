import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
move = [0] * 11

grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

queue = deque()
temp = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'o':
            temp.append((i, j))

temp.append(0)
queue.append(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while queue:
    first, second, count = queue.popleft()
    
    if count == 10:
        continue

    for i in range(4):
        temp = []

        fx = first[0] + dx[i]
        fy = first[1] + dy[i]

        sx = second[0] + dx[i]
        sy = second[1] + dy[i]

        if 0 <= fx < N and 0 <= fy < M:
            if grid[fx][fy] != '#':
                temp.append((fx, fy))
            else:
                temp.append((first[0], first[1]))
        else:
            move[count + 1] += 1

        if 0 <= sx < N and 0 <= sy < M:
            if grid[sx][sy] != '#':
                temp.append((sx, sy))
            else:
                temp.append((second[0], second[1]))
        else:
            move[count + 1] += 1
        
        temp.append(count + 1)

        if move[count + 1] == 0:
            queue.append(temp)
        elif move[count + 1] == 2:
            move[count + 1] = 0
        elif move[count + 1] == 1:
            queue = deque()
            break

for i in range(1, 11):
    if move[i] == 1:
        print(i)
        break
else:
    print(-1)

#### MORE SHORT TIME SOLVE ####
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int, input().split())

# coin = []

# matrix = []
# for i in range(N):
#     line = list(input())
#     for j in range(M):
#         if line[j] == 'o':
#             coin.append([i, j])
#     matrix.append(line)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

# def bfs():
#     dq = [(coin, 0)]
#     dq = deque(dq)

#     visited[coin[0][0]][coin[0][1]][coin[1][0]][coin[1][1]] = 1

#     while dq:
#         c, cnt = dq.popleft()
#         b = False
#         for i in range(4):
#             result = 0
#             nc = []
#             for j in range(2):
#                 nx = c[j][0] + dx[i]
#                 ny = c[j][1] + dy[i]
#                 if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                     result += 1
#                 else:
#                     if matrix[nx][ny] == "#":
#                         nc.append(c[j])
#                     else:
#                         nc.append([nx, ny])
#             if result == 1:
#                 print(cnt + 1)
#                 return
#             elif result == 0 and cnt+1 < 10 and visited[nc[0][0]][nc[0][1]][nc[1][0]][nc[1][1]] == 0:
#                 visited[nc[0][0]][nc[0][1]][nc[1][0]][nc[1][1]] = 1
#                 dq.append((nc, cnt+1))
#     else:
#         print(-1)
                
# bfs()
