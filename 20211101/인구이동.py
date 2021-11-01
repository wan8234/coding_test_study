from collections import deque

N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
day = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, union_idx, arr):

    union = []
    union.append((x, y))
    q = deque()
    q.append((x, y))
    open[x][y] = union_idx  # 연합 식별자
    population = arr[x][y]  # 연합 인구수
    union_cnt = 1   # 연합 수

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내, 연합에 안들어가있는 나라
            if 0 <= nx < N and 0 <= ny < N and open[nx][ny] == -1:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    q.append((nx, ny))
                    open[nx][ny] = union_idx
                    population += arr[nx][ny]
                    union_cnt += 1
                    union.append((nx, ny))

    for i, j in union:
        arr[i][j] = population // union_cnt


while True:
    open = [[-1] * N for _ in range(N)]
    union_idx = 0

    #전수 조사
    for i in range(N):
        for j in range(N):
            #조사한 나라여부 확인
            if open[i][j] == -1:
                bfs(i, j, union_idx, arr)
                union_idx += 1
    # 모든 인구 이동이 끝난 경우
    if union_idx == N * N:
        break
    day += 1

print(day)
