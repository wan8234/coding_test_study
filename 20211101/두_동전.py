import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

coin = []

matrix = []
for i in range(N):
    line = list(input())
    for j in range(M):
        if line[j] == 'o':
            coin.append([i, j])
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#방문확인
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

def bfs():
    dq = [(coin, 0)]
    dq = deque(dq)

    visited[coin[0][0]][coin[0][1]][coin[1][0]][coin[1][1]] = 1

    while dq:
        c, cnt = dq.popleft()
        for i in range(4):
            result = 0
            nc = []
            #코인 두개 위치 변경
            for j in range(2):
                nx = c[j][0] + dx[i]
                ny = c[j][1] + dy[i]
                #범위를 벗어나면 떨어진 것
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    #떨어진 동전 개수
                    result += 1
                else:
                    #벽이면 원래 위치값
                    if matrix[nx][ny] == "#":
                        nc.append(c[j])
                    #아니면 바뀐 위치 값
                    else:
                        nc.append([nx, ny])
            #떨어진 동전이 1개이면 끝
            if result == 1:
                print(cnt + 1)
                return
            #떨어진 동전이 0개이고 방문하지 않았을 때 dq 추가
            elif result == 0 and cnt+1 < 10 and visited[nc[0][0]][nc[0][1]][nc[1][0]][nc[1][1]] == 0:
                visited[nc[0][0]][nc[0][1]][nc[1][0]][nc[1][1]] = 1
                dq.append((nc, cnt+1))
    else:
        print(-1)

                
bfs()