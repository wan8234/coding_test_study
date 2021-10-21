from collections import deque

n = int(input())
arr = []
shark_lv = 2
exp = 0
res = 0
shark_x, shark_y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_x, shark_y = i, j
            arr[shark_x][shark_y] = 0


def bfs():
    d = [[-1] * n for i in range(n)]  # 최단거리
    q = deque([(shark_x, shark_y)])
    d[shark_x][shark_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 후 공간 내에 있을 조건
            if 0 <= nx < n and 0 <= ny < n:
                # 지나갈 수 있는 조건
                if d[nx][ny] == -1 and arr[nx][ny] <= shark_lv:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    return d


def search(d):
    x, y = 0, 0  # 물고기 좌표
    min_d = 99999  # 도달 불가 거리로 초기화
    for i in range(n):
        for j in range(n):
            # 물고기 판단
            if 0 < arr[i][j] < shark_lv and d[i][j] != -1:
                if d[i][j] < min_d:
                    x, y = i, j
                    min_d = d[i][j]
    if min_d == 99999:
        return None
    else:
        return x, y, min_d  # tuple 반환


while True:
    pos = search(bfs())

    # 엄마 상어 호출
    if pos is None:
        print(res)
        break
    else:
        # 물고기 사냥 및 위치 이동
        shark_x, shark_y = pos[0], pos[1]
        res += pos[2]
        exp += 1
        arr[shark_x][shark_y] = 0

        # 렙업 조건
        if exp >= shark_lv:
            shark_lv += 1
            exp = 0
