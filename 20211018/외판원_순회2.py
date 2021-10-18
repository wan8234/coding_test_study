import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

res = int(1e9)

def dfs(x, visited, cost):
    global res
    if res < cost:
        return
    if len(visited) == n and matrix[x][start] != 0:
        res = min(res, cost + matrix[x][start])
        return
    for i in range(n):
        if matrix[x][i] != 0 and i not in visited:
            visited.append(i)
            dfs(i, visited, cost + matrix[x][i])
            visited.pop()


for i in range(n):
    start = i
    visited = [i]
    dfs(i, visited, 0)


print(res)
