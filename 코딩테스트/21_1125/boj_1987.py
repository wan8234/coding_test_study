import sys

input = sys.stdin.readline

r,c = map(int,input().split())

board = [list(input().rstrip()) for _ in range(r)]

start_x,start_y = 0 ,0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 1


def bfs(x,y):

    global answer

    q = set([(0, 0, board[0][0])])
    

    while q:

        x,y,visited = q.pop()


        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:

                if board[nx][ny] not in visited:

                    q.add((nx,ny,visited + board[nx][ny]))

                    answer = max(answer,len(visited)+1)

bfs(start_x,start_y)

print(answer)



# python3 -> time over (only pypy)

'''
board = [list(map(lambda a : ord(a)-65,input())) for _ in range(r)]
visited = [0] * 26


start_x,start_y = 0 ,0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 1
visited[board[0][0]] = 1

def dfs(x,y,cnt):

    global answer

    answer = max(answer,cnt)

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[board[nx][ny]]:

                visited[board[nx][ny]] = 1

                dfs(nx,ny,cnt+1)

                visited[board[nx][ny]] = 0

dfs(start_x,start_y,answer)

print(answer)

'''