# 구슬은 좌, 우로만 움직일 수 있고 맨위 벽돌만 깨트릴 수 있음
# 벽돌은 1~9
# 충돌한 벽돌은 상하좌우로 벽돌에 적힌 숫자 - 1 칸 만큼 같이 제거됨
# 벽돌은 동시에 제거됨
# 빈 공간 있을 경우 벽돌은 밑으로 떨어짐
# N개 떨어뜨려 남은 벽돌의 개수 구하기

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def game(marble, boa):
    global result

    temp = count(boa)
    result = min(result, temp)
    if result == 0:
        return
    if marble == 0:
        return
    x, y = 0, 0
    scope = 0

    for w in range(W):
        queue = []

        for h in range(H):
            if boa[h][w] != 0:
                x = h
                y = w
                scope = boa[x][y]
                queue.append([x, y, scope])
                break

        board_copy = [b[:] for b in boa]
        
        while queue:
            px, py, scope = queue.pop(0)

            board_copy[px][py] = 0
            
            if scope == 1:
                continue

            for i in range(4):
                for j in range(1, scope):
                    nx = px + j * dx[i]
                    ny = py + j * dy[i]

                    if 0 <= nx < H and 0 <= ny < W and board_copy[nx][ny] != 0:
                        if [nx, ny, board_copy[nx][ny]] not in queue:
                            queue.append([nx, ny, board_copy[nx][ny]])

        for w in range(W):
            temp = []
            for h in range(H):
                if board_copy[h][w] != 0:
                    temp.append(board_copy[h][w])
            
            length = H - len(temp)
            li = [0] * length
            li.extend(temp)

            for h in range(H):
                board_copy[h][w] = li[h]
        
        game(marble - 1, board_copy)   
    

def count(boa):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if boa[i][j] != 0:
                cnt += 1
    
    return cnt

T = int(input())

for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())    
    result = H * W
    board = [list(map(int, input().split())) for _ in range(H)]

    game(N, board)

    print('#{} {}'.format(test_case, result))

# 5
# 3 10 10
# 0 0 0 0 0 0 0 0 0 0
# 1 0 1 0 1 0 0 0 0 0
# 1 0 3 0 1 1 0 0 0 1
# 1 1 1 0 1 2 0 0 0 9
# 1 1 4 0 1 1 0 0 1 1
# 1 1 4 1 1 1 2 1 1 1
# 1 1 5 1 1 1 1 2 1 1
# 1 1 6 1 1 1 1 1 2 1
# 1 1 1 1 1 1 1 1 1 5
# 1 1 7 1 1 1 1 1 1 1
# 2 9 10
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 1 1 0 0 1 0 0 0 0
# 1 1 0 1 1 1 0 1 0
# 1 1 0 1 1 1 0 1 0
# 1 1 1 1 1 1 1 1 0
# 1 1 3 1 6 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 3 6 7
# 1 1 0 0 0 0
# 1 1 0 0 1 0
# 1 1 0 0 4 0
# 4 1 0 0 1 0
# 1 5 1 0 1 6
# 1 2 8 1 1 6
# 1 1 1 9 2 1
# 4 4 15
# 0 0 0 0 
# 0 0 0 0 
# 0 0 0 0 
# 1 0 0 0 
# 1 0 0 0 
# 1 0 0 0 
# 1 0 0 0 
# 1 0 5 0 
# 1 1 1 0 
# 1 1 1 9 
# 1 1 1 1 
# 1 6 1 2 
# 1 1 1 5 
# 1 1 1 1 
# 2 1 1 2 
# 4 12 15
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
# 9 9 9 9 9 9 9 9 9 9 9 9
