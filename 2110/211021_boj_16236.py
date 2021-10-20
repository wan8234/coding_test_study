from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
space = []
shark = 2
count = 0
time = 0
x, y = 0, 0

for _ in range(n):
    space.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            x, y = i, j

space[x][y] = 0

def bfs():
    global shark
    global x
    global y
    global count

    queue = deque()
    queue.append([x, y])
    visit = [[0] * n for _ in range(n)]
    visit[x][y] = 1
    eat = []
    dist = [[0] * n for _ in range(n)]

    while queue:
        px, py = queue.popleft()
        
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if space[nx][ny] <= shark or space[nx][ny] == 0:
                    queue.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[px][py] + 1
                if space[nx][ny] < shark and space[nx][ny] != 0:
                    eat.append([dist[nx][ny], nx, ny])

    if eat == []:
        return False

    eat.sort()

    x, y= eat[0][1], eat[0][2]
    count += 1

    if count == shark:
        shark += 1
        count = 0
    space[x][y] = 0
    
    return eat[0][0]

while True:
    use = bfs()
    if use == 0:
        break
    time += use

print(time)
