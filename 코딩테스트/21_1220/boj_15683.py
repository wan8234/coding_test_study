import sys
import copy

input = sys.stdin.readline


n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

cctv = []
cctv_cnt = 0

answer = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direction = [[],
             [[0], [1], [2], [3]],                          # cctv 1
             [[0, 1], [2, 3]],                              # cctv 2
             [[0, 2], [1, 2], [1, 3], [0, 3]],              # cctv 3
             [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],  # cctv 4
             [[0, 1, 2, 3]]                                 # cctv 5
             ]

# cctv 위치 저장
for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            cctv.append((i, j, board[i][j])) # x, y, cctv 타입 저장(1~5)
            cctv_cnt += 1

def dfs(map, depth):

    global answer
    tmp = copy.deepcopy(map)

    if depth == cctv_cnt: # dfs로 모든 cctv 탐색 완료시

        temp = 0

        for i in range(n): #사각지대 카운트
            for j in range(m):
                if tmp[i][j] == 0:
                    temp += 1

        answer = min(answer, temp) 
        return
 
    x, y, cctv_type = cctv[depth]

    for ds in direction[cctv_type]: # 각 cctv별 감시방향 탐색

        for d in ds:

            nx, ny = x, y # nx, ny 선언

            while True:

                nx += dx[d] # dx[d] 방향으로 탐색
                ny += dy[d] 

                if 0 <= nx < n and 0 <= ny < m: # 그래프 범위 안에서만 계속 나아감

                    if tmp[nx][ny] != 6: # 벽이 없다는 조건에
                        if tmp[nx][ny] == 0: # 이동할 공간이 0 이면
                            tmp[nx][ny] = '#' # cctv의 감시 지대임

                    else: # 벽(6) 만나면 # 더이상 작성 안함
                        break
                else:
                    break

        dfs(tmp, depth + 1) #모든 cctv를 탐색할때까지 dfs 재귀

        tmp = copy.deepcopy(map) # 탐색 후 tmp 다시 초기화

dfs(board,0)

print(answer)