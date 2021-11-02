import sys
input = sys.stdin.readline
from collections import deque

field = [list(input().rstrip()) for _ in range(12)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visit = [[0] * 6 for _ in range(12)]
flag = 1 # 연쇄 여부 확인
answer = 0

def crush(x, y): # 연쇄 함수
    global field, visit, flag
    queue = deque()
    queue.append((x, y))
    color = field[x][y]
    union = []
    union.append((x, y))

    visit[x][y] = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and not visit[nx][ny] and field[nx][ny] == color:
                visit[nx][ny] = 1
                queue.append((nx, ny))
                union.append((nx, ny))
    
    if len(union) >= 4:
        flag = 1
        for ux, uy in union:
            field[ux][uy] = '.'

def arrange(): # 정렬 함수
    global field

    temp = [['.'] * 6 for _ in range(12)]
    
    for i in range(6):
        index = 11
        for j in range(11, -1, -1):
            if field[j][i] != '.':
                temp[index][i] = field[j][i]
                index -= 1

    field = temp

while flag: # 연쇄 된적 있을 경우 반복
    visit = [[0] * 6 for _ in range(12)]
    flag = 0

    for i in range(12):
        for j in range(6):
            if not visit[i][j] and field[i][j] != '.':                
                crush(i, j)
            visit[i][j] = 1
    arrange()
    if flag:
        answer += 1    

print(answer)

