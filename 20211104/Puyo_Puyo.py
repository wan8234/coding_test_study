import sys
input = sys.stdin.readline
from collections import deque

matrix = []
visited = [[0] * 6 for _ in range(12)]

for _ in range(12):
    x = list(input().strip('\n'))
    matrix.append(x)

def bfs(dq):
    global matrix, visited
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    b = []
    result = False
    while dq:
        x, y, char = dq.popleft()
        b.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == 0 and matrix[nx][ny] == char:
                dq.append((nx, ny, matrix[nx][ny]))
                visited[nx][ny] = 1
    
    if len(b) >= 4:
        result = True
        for x, y in b:
            matrix[x][y] = "."

    return result
        
answer = 0

def bomb():
    global visited
    visited = [[0] * 6 for _ in range(12)]
    dq = deque()
    finish = True
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != "." and visited[i][j] == 0:
                dq.append((i, j, matrix[i][j]))
                visited[i][j] = 1
                result = bfs(dq)
                if result:
                    finish = False
    return finish

def fall():
    global matrix
    for i in range(6):
        temp = deque()
        for j in range(11, -1, -1):
            if matrix[j][i] != ".":
                temp.append(matrix[j][i])
                matrix[j][i] = "."
        for j in range(11, -1, -1):
            if not temp:
                break
            c = temp.popleft()
            matrix[j][i] = c


while True:
    
    if bomb():
        break
    else:
        answer += 1
        fall()



print(answer)