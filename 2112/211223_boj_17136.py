import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
inf = int(1e9)

board = [list(map(int, input().split())) for _ in range(10)]
many = [0] * 5
result = inf

def dfs(x, y, cnt):
    global many, result

    if x >= 10:
        result = min(result, cnt)
        return
    
    if y >= 10:
        dfs(x + 1, 0, cnt)
        return
    
    if board[x][y] == 1:
        for i in range(5):
            if many[i] == 5:
                continue
            if x + i >= 10 or y + i >= 10:
                continue

            flag = True
            for m in range(x, x + i + 1):
                for n in range(y, y + i + 1):
                    if board[m][n] == 0:
                        flag = False
                        break
                if not flag:
                    break

            if flag:
                for m in range(x, x + i + 1):
                    for n in range(y, y + i + 1):
                        board[m][n] = 0
                many[i] += 1
                dfs(x, y + i + 1, cnt + 1)

                many[i] -= 1
                for m in range(x, x + i + 1):
                    for n in range(y, y + i + 1):
                        board[m][n] = 1
    else:
        dfs(x, y + 1, cnt)

dfs(0, 0, 0)
print(result if result != inf else -1)