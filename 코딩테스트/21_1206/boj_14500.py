import sys

input = sys.stdin.readline

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


visited = [([False] * m) for _ in range(n)]

answer = 0
max_val = max(map(max, board))


def dfs(x,y,depth,score):


    global answer

    if answer >= score + max_val * (4 - depth): # 남은 블럭이 모두 최댓값이라 해도 현재의 최댓값를 넘길수 없을때 조기종료 
        return  

    if depth == 4:
        answer = max(answer,score)
        return

    else:

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]


            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False:

                    if depth == 2: #ㅗ자 처리하기위해서 depth가 2일때 자기자신을 dfs로 다시 호출

                        visited[nx][ny] = True

                        dfs(x,y,depth + 1,score+board[nx][ny])

                        visited[nx][ny] = False   

                    visited[nx][ny] = True

                    dfs(nx,ny,depth + 1,score+board[nx][ny])

                    visited[nx][ny] = False 


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,board[i][j])
        visited[i][j] = False

print(answer)


######### 노가다 코드 5392ms #########
'''

answer = 0

tetromiro_blocks = [
    [(0,1), (1,0), (1,1)], #네모
    [(0,1), (0,2), (0,3)], #가로
    [(1,0), (2,0), (3,0)], #세로
    [(0,1), (0,2), (1,0)], #ㄱ자1
    [(0,1), (0,2), (-1,2)], #ㄱ자2
    [(1,0), (1,1), (1,2)], #ㄱ자3
    [(0,1), (0,2), (1,2)], #ㄱ자4
    [(1,0), (2,0), (2,1)], #ㄱ자5
    [(0,1), (1,1), (2,1)], #ㄱ자6
    [(0,1), (1,0), (2,0)], #ㄱ자7
    [(1,0), (2,0), (2,-1)], #ㄱ자8
    [(1,0), (1,1), (2,1)], #번개모양1
    [(0,1), (1,0), (-1,1)], #번개모양2
    [(0,1), (1,0), (1,-1)], #번개모양3
    [(0,1), (1,1), (1,2)], #번개모양4
    [(0,1), (0,2), (1,1)], #ㅜ자
    [(1,0), (1,1), (1,-1)], #ㅗ자
    [(1,0), (2,0), (1,-1)], #ㅓ자
    [(1,0), (1,1), (2,0)] #ㅏ 자
]


def find_max(x,y):

    global answer

    for i in range(len(tetromiro_blocks)):

        cur_score = board[x][y]

        for j in range(3): #현재위치 + 3블록

            nx = x + tetromiro_blocks[i][j][0]
            ny = y + tetromiro_blocks[i][j][1]

            if 0 <= nx < n and 0 <= ny < m:
                cur_score += board[nx][ny]

        answer = max(cur_score,answer)


for i in range(n):
    for j in range(m):
        find_max(i,j)


print(answer)'''