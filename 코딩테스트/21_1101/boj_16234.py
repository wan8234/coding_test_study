import sys
sys.setrecursionlimit(100000) 

input = sys.stdin.readline

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def sol():

    cnt = 0

    def dfs(x, y):

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and check[nx][ny]:
                if L <= abs(maps[x][y] - maps[nx][ny]) <= R:

                    check[nx][ny] = False
                    union.append([nx, ny])
                    dfs(nx, ny)

    while True:

        check = [[True] * N for _ in range(N)] 
        flag = True

        for i in range(N):
            for j in range(N):

                union = []

                if check[i][j]:

                    union.append([i, j])
                    check[i][j] = False
                    dfs(i, j)

                    if len(union) > 1:

                        flag = False
                        avg = sum([maps[x][y] for x, y in union]) // len(union)

                        for x, y in union:

                            maps[x][y] = avg

        if flag: 
            
            break

        cnt += 1

    return cnt

print(sol())