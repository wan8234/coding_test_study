import sys
input = sys.stdin.readline
# sys.setrecursionlimit(99999)

N, L, R = map(int, input().split())
land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

# dx = [0, 1, 0, -1] # 해당 순서로 할 경우 recursion error에 걸림
# dy = [1, 0, -1, 0]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0] * N for _ in range(N)]

def dfs(x, y):
    global union, total, visit

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and L <= abs(land[nx][ny] - land[x][y]) <= R:
            union.append((nx, ny))
            visit[nx][ny] = 1
            total += land[nx][ny]
            dfs(nx, ny)

answer = 0
while True:
    visit = [[0] * N for _ in range(N)]
    check = 0

    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                union = [(i, j)]
                total = land[i][j]

                dfs(i, j)

                if len(union) < 2:
                    check += 1
                else:
                    for x, y in union:
                        land[x][y] = total // len(union)

    if check == N * N:
        print(answer)
        break
    answer += 1

#### USING BFS ####

# from collections import deque
# import sys
# input = sys.stdin.readline

# N, L, R = map(int, input().split())
# countries = [list(map(int, input().split())) for _ in range(N)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def check(r, c, ans):
#     q = deque()
#     q.append([r, c])
#     temp = []

#     while q:
#         r, c = q.popleft()
#         for k in range(4):
#             nr, nc = r + dx[k], c + dy[k]
#             if 0 <= nr < N and 0 <= nc < N and border[nr][nc] != ans:
#                 if L <= abs(countries[r][c] - countries[nr][nc]) <= R:
#                     border[nr][nc] = ans
#                     q.append([nr, nc])
#                     temp.append([nr, nc])
#     return temp

# search = deque()
# for i in range(N):
#     for j in range(N):
#         search.append([i, j])

# border = [[-1 for _ in range(N)] for _ in range(N)]
# ans = 0

# while True:
#     state = False
#     for _ in range(len(search)):
#         i, j = search.popleft()
#         if border[i][j] != ans:
#             temp = check(i, j, ans)
#             if len(temp) > 1:
#                 state = True
#                 num = sum([countries[r][c] for r, c in temp])
#                 mean = num // len(temp)
#                 for r, c in temp:
#                     countries[r][c] = mean
#                     search.append([r,c])
#     if not state:
#         print(ans)
#         break
#     else:
#         ans += 1