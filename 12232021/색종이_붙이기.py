import sys
input = sys.stdin.readline
INF = int(1e9)
sys.setrecursionlimit(10**9)

graph = [list(map(int, input().split())) for _ in range(10)]
arr = [0] * 5
answer = INF

def dfs(x, y, cnt):
    global arr, answer

    if x >= 10:
        answer = min(answer, cnt)
        return
    
    if y >= 10:
        dfs(x + 1, 0, cnt)
        return
    
    if graph[x][y]:
        for i in range(5):
            if arr[i] == 5:
                continue
            if x + i >= 10 or y + i >= 10:
                continue
            flag = True

            for m in range(x, x + i + 1):
                for n in range(y, y + i + 1):
                    if graph[m][n] == 0:
                        flag = False
                        break
                if not flag:
                    break

            if flag:
                for m in range(x, x + i + 1):
                    for n in range(y, y + i + 1):
                        graph[m][n] = 0
                arr[i] += 1
                dfs(x, y + i + 1, cnt + 1)
                arr[i] -= 1
                for m in range(x, x + i + 1):
                    for n in range(y, y + i + 1):
                        graph[m][n] = 1
    else:
        dfs(x, y + 1, cnt)

dfs(0, 0, 0)

if answer != INF:
    print(answer)
else:
    print(-1)

