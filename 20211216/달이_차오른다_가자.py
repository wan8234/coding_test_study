import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
matrix = []
S = 0
for i in range(N):
    line = list(input().strip('\n'))
    for j in range(M):
        if line[j] == '0':
            S = (i, j)
    matrix.append(line)


key = ['0'] * 6
dq = deque([(S[0], S[1], 0, key)])

visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


while dq:
    x, y, cnt, k = dq.popleft()
    B = False
    intkey = int(''.join(k), 2)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != '#' and visited[nx][ny][intkey] == 0:
            #탈출
            if matrix[nx][ny] == '1':
                print(cnt+1)
                B = True
                break

            if matrix[nx][ny] == '.' or matrix[nx][ny] == '0':
                dq.append((nx, ny, cnt+1, k))
                visited[nx][ny][intkey] = 1

            #대문자(문)
            elif ord(matrix[nx][ny]) - ord('a') < 0:
                if k[ord(matrix[nx][ny]) - ord('A')] == '1':
                    dq.append((nx, ny, cnt+1, k))
                    visited[nx][ny][intkey] = 1

            #소문자(키)
            else:
                newk = k[:]
                #키 보유
                newk[ord(matrix[nx][ny]) - ord('a')] = '1'
                dq.append((nx, ny, cnt+1, newk))
                newintkey = int(''.join(newk), 2)
                visited[nx][ny][newintkey] = 1
    if B:
        break
else:
    print(-1)
    
