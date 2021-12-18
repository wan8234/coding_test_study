import copy
import sys
input = sys.stdin.readline
inf = int(1e9)

dx = [0, 1, 0, -1] # 우 0, 하 1, 좌 2, 상 3
dy = [1, 0, -1, 0]
direction = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0 ,1]], [[0, 1, 2, 3]]]

N, M = map(int, input().split())

board = []
cctv_count = 0
cctvs = []
result = inf

for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)

    for j in range(M):
        if 1 <= line[j] <= 5:
            cctvs.append([i, j, line[j]])
            cctv_count += 1

def vision(x, y, direct, temp):
    for d in direct:
        nx = x
        ny = y

        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
            else:
                break

def dfs(board, count):
    global result

    if count == cctv_count:
        check = 0
        for b in board:
            check += b.count(0)
        result = min(result, check)
        return
    
    x, y, cctv = cctvs[count]
    for direct in direction[cctv]:        
        temp = copy.deepcopy(board)
        vision(x, y, direct, temp)
        dfs(temp, count + 1)

dfs(board, 0)
print(result)