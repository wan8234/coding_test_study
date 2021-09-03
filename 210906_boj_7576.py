from collections import deque 

m, n = map(int, input().split())
queue = deque()
tomato = []
day = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    temp = list(map(int, input().split()))
    tomato.append(temp)

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j, 0])

while queue:
    cur_x, cur_y, date = queue.popleft()
    day = date

    for i in range(4):
        new_x, new_y = cur_x + dx[i], cur_y + dy[i]
        if new_x >= n or new_y >= m or new_x < 0 or new_y < 0:
            continue
        elif tomato[new_x][new_y] == 0:
            tomato[new_x][new_y] = 1
            queue.append([new_x, new_y, date + 1])
            
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            day = -1
            break
    if day == -1:
        break

print(day)
