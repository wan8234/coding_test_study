from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
pipe = [[(1, 0), (-1, 0), (0, 1), (0, -1)], [(-1, 0), (1, 0)], [(0, 1), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]]

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, mx, my, L = map(int, input().split())
    matrix = []
    for _ in range(N):
        line = list(map(int, input().split()))
        matrix.append(line)

    check = [[0] * M for _ in range(N)]
    dq = deque([(mx, my, 1)])
    check[mx][my] = 1
    
    res = 0

    while dq:
        x, y, cnt = dq.popleft()
        res += 1
        p = pipe[matrix[x][y] - 1]
        for r, c in p:
            nx = x + r
            ny = y + c
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] > 0 and cnt < L and check[nx][ny] == 0 and (-r, -c) in pipe[matrix[nx][ny] - 1]:
                dq.append((nx, ny, cnt+1))
                check[nx][ny] = 1
    print("#", test_case+1, " ", res, sep="")