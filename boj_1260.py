n, m, v = map(int, input().split())

vertex = [[] for _ in range(n + 1)]
visit = [[0] for _ in range(n + 1)]

for _ in range(m):
    first, second = map(int, input().split())

    vertex[first].append(second)
    vertex[second].append(first)

def dfs(v):
    print(v, end = " ")
    visit[v] = 1
    for node in vertex[v]:
        if