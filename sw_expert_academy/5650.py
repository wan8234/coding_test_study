# N*N 크기 핀볼판
# 정사각형 블록과 4가지 형태의 삼각형 블록들 섞여 있음
# 웜홀과 블랙홀 존재
# 상하좌우 중 한 방향으로 이동
# 경사면과 부딪히면 직각 회전
# 벽과 만나면 반대로 튕김
# 웜홀 만나면 동일한 숫자 가진 다른 웜홀로 빠져나옴, 진행방향 유지
# 블랙홀 만나면 사라짐
# 블랙홀 만나거나 시작 위치로 돌아오면 게임 종료
# 점수는 벽이나 블록에 부딪힌 횟수
# 게임에서 얻을 수 잇는 점수 최댓값
# 단 시작은 빈 공간에서만 가능

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

block = [[], [2, 0, 3, 1], [2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 3, 0, 1]]
wall = [2, 3, 0, 1]

def bfs(x, y, direct):
    global result
    queue = [[x, y, direct]]
    score = 0
    
    while queue:
        px, py, d = queue.pop(0)

        nx = px + dx[d]
        ny = py + dy[d]

        if 0 <= nx < N and 0 <= ny < N: # 게임판 범위
            if nx == x and ny == y:
                return score
            else:
                if board[nx][ny] == 0: # 빈공간
                    queue.append([nx, ny, d])
                elif board[nx][ny] == -1: # 블랙홀
                    return score
                elif 6 <= board[nx][ny] <= 10: # 웜홀
                    for position in worm[board[nx][ny]]:
                        if (nx, ny) != position:
                            queue.append([position[0], position[1], d])
                elif 1 <= board[nx][ny] <= 5: # 블록
                    score += 1
                    queue.append([nx, ny, block[board[nx][ny]][d]])

        else: # 벽 부딪힘
            score += 1
            queue.append([nx, ny, wall[d]])                

T = int(input())

for test_case in range(1, T + 1):
    result = 0

    N = int(input())
    board = []
    worm = {}

    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                if board[i][j] in worm:
                    worm[board[i][j]].append((i, j))
                else:
                    worm[board[i][j]] = [(i, j)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for d in range(4):
                    score = bfs(i, j, d)
                    result = max(result, score)

    print('#{} {}'.format(test_case, result))

# 5
# 10
# 0 1 0 3 0 0 0 0 7 0 
# 0 0 0 0 -1 0 5 0 0 0 
# 0 4 0 0 0 3 0 0 2 2 
# 1 0 0 0 1 0 0 3 0 0 
# 0 0 3 0 0 0 0 0 6 0 
# 3 0 0 0 2 0 0 1 0 0 
# 0 0 0 0 0 1 0 0 4 0 
# 0 5 0 4 1 0 7 0 0 5 
# 0 0 0 0 0 1 0 0 0 0 
# 2 0 6 0 0 4 0 0 0 4 
# 6
# 1 1 1 1 1 1 
# 1 1 -1 1 1 1 
# 1 -1 0 -1 1 1 
# 1 1 -1 1 1 1 
# 1 1 1 1 1 1 
# 1 1 1 1 1 1 
# 8
# 0 0 0 3 0 0 0 0 
# 0 0 2 0 0 5 0 0 
# 0 0 5 0 3 0 0 0 
# 0 0 1 1 0 0 0 4 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 5 0 
# 0 0 4 0 0 3 1 0 
# 2 0 0 4 3 4 0 0 
# 10
# 0 4 0 0 0 0 4 0 5 0 
# 0 0 0 0 0 0 0 0 3 0 
# 0 0 0 5 6 0 0 0 0 2 
# 3 0 0 1 0 0 1 4 0 2 
# 2 0 0 0 0 5 0 0 5 0 
# 0 0 1 0 2 0 0 0 5 0 
# 0 0 0 0 0 0 6 1 0 0 
# 0 0 1 0 2 0 2 4 0 0 
# 0 0 0 0 0 0 2 0 0 0 
# 2 0 0 0 0 0 0 3 0 0 
# 20
# 0 0 1 0 0 0 0 3 0 3 0 0 0 4 0 0 1 0 4 0 
# 0 1 2 3 3 0 0 0 0 0 0 0 0 5 0 0 0 0 5 0 
# 0 0 0 0 0 0 0 0 0 5 0 0 0 5 0 4 0 0 0 0 
# 4 0 0 0 0 0 0 4 5 0 0 0 3 0 0 0 3 0 0 0 
# 0 0 0 3 0 4 1 0 3 0 0 0 0 4 0 0 0 2 0 3 
# 2 2 0 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 5 0 5 0 0 0 3 4 
# 0 0 5 0 -1 5 0 0 5 2 0 0 0 4 2 0 0 3 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 
# 2 0 0 0 0 3 0 0 3 3 3 0 0 1 0 0 2 0 0 0 
# 1 5 0 5 0 0 0 0 5 4 5 0 0 0 0 4 2 4 0 0 
# 0 4 0 0 0 1 3 0 0 0 0 0 1 0 3 0 0 2 0 0 
# 0 0 0 0 0 0 3 0 1 0 0 1 0 0 0 0 0 3 4 0 
# 0 4 0 4 0 0 0 0 0 0 0 2 0 0 0 3 0 0 0 2 
# 0 5 0 0 0 4 1 5 0 0 0 2 0 0 0 0 0 0 0 0 
# 0 0 0 5 0 0 1 2 0 0 0 3 1 2 5 0 0 0 0 0 
# 0 4 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 4 0 0 0 0 4 0 0 0 0 0 0 1 4 0 2 0 
# 0 0 1 0 0 0 0 0 3 0 0 0 0 0 0 0 5 0 0 0 
# 0 0 0 0 0 0 0 5 0 4 0 0 0 0 0 2 0 0 2 0 
