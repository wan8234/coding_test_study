import sys
from collections import deque

input = sys.stdin.readline


n,m = map(int,input().split())

board = [list(input().rstrip()) for _ in range(n)]


Rx,Ry,Bx,By = 0,0,0,0

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1] 

q = deque()


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            Rx,Ry = i,j
        if board[i][j] == 'B':
            Bx,By = i,j

q.append((Rx, Ry, Bx, By, 0))
visited[Rx][Ry][Bx][By] = True

def move(x,y,dx,dy,dist):

    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':

        x += dx
        y += dy
        dist +=1

    return x,y,dist


while q:

    rx, ry, bx, by, move_dist = q.popleft()import sys
from collections import deque

input = sys.stdin.readline


n,m = map(int,input().split())

board = [list(input().rstrip()) for _ in range(n)]


Rx,Ry,Bx,By = 0,0,0,0

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1] 

q = deque()


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            Rx,Ry = i,j
        if board[i][j] == 'B':
            Bx,By = i,j

q.append((Rx, Ry, Bx, By, 0))
visited[Rx][Ry][Bx][By] = True

def move(x,y,dx,dy,dist):

    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':

        x += dx
        y += dy
        dist +=1

    return x,y,dist


while q:

    rx, ry, bx, by, move_dist = q.popleft()

    if move_dist >= 10:
        break

    for i in range(len(dx)):

        nrx,nry,r_dist = move(rx,ry,dx[i],dy[i],0)
        nbx,nby,b_dist = move(bx,by,dx[i],dy[i],0)

        if board[nbx][nby] == 'O': # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
            continue

        if board[nrx][nry] == 'O':
            print(1)
            sys.exit(0)

        if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면

            if r_dist > b_dist: # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동

                nrx -= dx[i]
                nry -= dy[i]

            else:
                nbx -= dx[i]
                nby -= dy[i]

        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            q.append((nrx, nry, nbx, nby, move_dist+1))

print(0)


    if move_dist >= 10:
        break

    for i in range(len(dx)):

        nrx,nry,r_dist = move(rx,ry,dx[i],dy[i],0)
        nbx,nby,b_dist = move(bx,by,dx[i],dy[i],0)

        if board[nbx][nby] == 'O':
            continue

        if board[nrx][nry] == 'O':
            print(1)
            sys.exit(0)

        if nrx == nbx and nry == nby:

            if r_dist > b_dist:
                nrx, nry = nrx-dx[i], nry-dy[i]

            else:
                nbx, nby = nbx-dx[i], nby-dy[i]

        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            q.append((nrx, nry, nbx, nby, move_dist+1))

print(0)
