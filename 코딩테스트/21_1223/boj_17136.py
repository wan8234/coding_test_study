import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 0, 0, 0, 0]
INF = int(1e9)
answer =  INF


def dfs(x, y, cnt):

    global answer

    if y >= 10:
        answer = min(answer, cnt)
        return

    if x >= 10:
        dfs(0, y + 1, cnt)
        return

    if board[x][y]:

        for p in range(5):
            if paper[p] == 5: 
                continue
            if x + p >= 10 or y + p >= 10: 
                continue
            flag = 0
            for i in range(x, x + p + 1):
                for j in range(y, y + p + 1):
                    if not board[i][j]: 
                        flag = 1
                        break
                if flag: break
            if not flag: 
                for i in range(x, x + p + 1):
                    for j in range(y, y + p + 1):
                        board[i][j] = 0

                paper[p] += 1
                dfs(x + p + 1, y, cnt + 1) 
                paper[p] -= 1

                for i in range(x, x + p + 1):
                    for j in range(y, y + p + 1):
                        board[i][j] = 1
    else: 
        dfs(x + 1, y, cnt)

dfs(0, 0, 0)

if answer == INF:
    print(-1)

else:
    print(answer)