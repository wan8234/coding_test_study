import sys
input = sys.stdin.readline


N, L, R = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

chk = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0

def dfs(x, y):
    global union, total, chk
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        #인구차이
        if 0 <= nx < N and 0 <= ny < N and chk[nx][ny] == 0 and L <= abs(matrix[x][y] - matrix[nx][ny]) <= R:
            #x,y에 대한 연합 국가 리스트
            union.append((nx, ny))
            chk[nx][ny] = 1
            #연합국가에 대한 인구 총합
            total += matrix[nx][ny]
            dfs(nx, ny)

while True:
    chk = [[0] * N for _ in range(N)]
    fin = 0
    #모든 국가에 대해 검사
    for i in range(N):
        for j in range(N):
            if chk[i][j] == 0:
                chk[i][j] = 1
                union = [(i, j)]
                total = matrix[i][j]
                #연합구하기
                dfs(i, j)
                #연합국이 없는 나라 세기
                if len(union) < 2:
                    fin += 1
                else:
                    #연합국에 대해 인구 분배
                    for x, y in union:
                        matrix[x][y] = total // len(union)
    else:
        #모두 연합국이 없으면 끝
        if fin == N*N:
            print(res)
            break
        res += 1
              