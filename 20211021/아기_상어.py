import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
matrix = []
px, py = 0, 0
size, eat = 2, 0
time = 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            px, py = i, j
    matrix.append(line)
    

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]  

matrix[px][py] = 0


def move():
    global px, py, fish, size, eat, time
    check = [[0] * n for _ in range(n)]
    dq = deque([(px, py, 0)])
    check[px][py] = 1
    distance = 0
    prey = []
    while dq:
        x, y, cnt = dq.popleft()
        #먹이 있는데 cnt가 거리를 넘어섰다면 break (가장 가까운 거리의 먹이를 먹어야 하므로)
        if len(prey) != 0 and cnt > distance:
            break
        #먹이 없을 때 현재 거리 저장
        elif len(prey) == 0 and cnt > distance:
            distance = cnt

        #내 사이즈보다 작으면 먹이 append
        if 0 < matrix[x][y] < size:
            prey.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #check 확인, 내 사이즈보다 작거나 같은지 확인
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 and matrix[nx][ny] <= size:
                check[nx][ny] = 1
                dq.append((nx, ny, cnt + 1))
    
    if len(prey) != 0:
        #조건대로 정렬
        prey.sort()

        #거리가 같은 먹이들 중 조건에 따라 먹이 선택    
        px, py = prey[0]
        time += distance
        matrix[px][py] = 0
        eat += 1
    else:
        #더 이상 먹을 수 있는 먹이가 없다!
        print(time)
        return True
    

while True:
    if move():
        break
    #사이즈 증가
    if size == eat:
        size += 1
        eat = 0

