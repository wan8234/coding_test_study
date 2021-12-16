import sys
from collections import deque

input = sys.stdin.readline

R,C = map(int,input().split())

board = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for i in range(R)]

dx=[1,0,-1,0]
dy=[0,-1,0,1]

q = deque()

for i in range(R):
    for j in range(C):

        if board[i][j] == 'S': #고슴도치 시작위치
            q.append([i, j, 's', 0])
            visited[i][j] = True

        elif board[i][j] == '*': #물 범람 시작위치
            q.appendleft([i, j, 'w', 0])
            visited[i][j] = True

def bfs():

    while q:
        x, y, type, cnt = q.popleft()

        if board[x][y] == 'D':
            return cnt

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i] 

            if 0 <= nx < R and 0 <= ny < C: 
              if not visited[nx][ny] and board[nx][ny] != 'X':
                if (type == 'w' and board[nx][ny] != 'D') or (type == 's' and board[nx][ny] != '*'):
                    
                    q.append([nx, ny, type, cnt + 1])
                    visited[nx][ny] = True

    return 'KAKTUS'


print(bfs())
