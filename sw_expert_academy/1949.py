dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(graph, visit, length, con, x, y):
    current = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] < current and visit[nx][ny] == 0: # mountain height is low
                visit[nx][ny] = 1
                dfs(graph, visit, length + 1, con, nx, ny)
                visit[nx][ny] = 0
            elif graph[nx][ny] >= current and visit[nx][ny] == 0: # mountain height is same or higher
                temp = graph[nx][ny] - current
                con -= (temp + 1)
                if con >= 0:
                    tgraph = graph[nx][ny]
                    graph[nx][ny] = current - 1
                    visit[nx][ny] = 1
                    dfs(graph, visit, length + 1, 0, nx, ny) # construct can be done only once
                    graph[nx][ny] = tgraph
                    visit[nx][ny] = 0
                con += (temp + 1)
    else:
        global result
        result = max(result, length)
        
T = int(input())

for test_case in range(1, T + 1):
    graph = []
    result = 0
    maximum = 0
    n, construct = map(int, input().split())
    visit = [[0] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    for g in graph:
        temp = max(g)
        maximum = max(maximum, temp)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == maximum:
                visit[i][j] = 1
                dfs(graph, visit, 1, construct, i, j)
                visit[i][j] = 0
    print('#'+ str(test_case) + ' ' + str(result))

# 10
# 5 1
# 9 3 2 3 2
# 6 3 1 7 5
# 3 4 8 9 9
# 2 3 7 7 7
# 7 6 5 5 8
# 3 2
# 1 2 1
# 2 1 2
# 1 2 1
# 5 2
# 9 3 2 3 2
# 6 3 1 7 5
# 3 4 8 9 9
# 2 3 7 7 7
# 7 6 5 5 8
# 4 4
# 8 3 9 5
# 4 6 8 5
# 8 1 5 1
# 4 9 5 5
# 4 1
# 6 6 1 7
# 3 6 6 1
# 2 4 2 4
# 7 1 3 4
# 5 5
# 18 18 1 8 18
# 17 7 2 7 2
# 17 8 7 4 3
# 17 9 6 5 16
# 18 10 17 13 18
# 6 4
# 12 3 12 10 2 2
# 13 7 13 3 11 6
# 2 2 6 5 13 9
# 1 12 5 4 10 5
# 11 10 12 8 2 6
# 13 13 7 4 11 7
# 7 3
# 16 10 14 14 15 14 14
# 15 7 12 2 6 4 9
# 10 4 11 4 6 1 1
# 16 4 1 1 13 9 14
# 3 12 16 14 8 13 9
# 3 4 17 15 12 15 1
# 6 6 13 6 6 17 12
# 8 5
# 2 3 4 5 4 3 2 1
# 3 4 5 6 5 4 3 2
# 4 5 6 7 6 5 4 3
# 5 6 7 8 7 6 5 4
# 6 7 8 9 8 7 6 5
# 5 6 7 8 7 6 5 4
# 4 5 6 7 6 5 4 3
# 3 4 5 6 5 4 3 2
# 8 2
# 5 20 15 11 1 17 10 14
# 1 1 11 16 1 14 7 5
# 17 2 3 4 5 13 19 20
# 6 18 5 16 6 7 8 5
# 10 4 5 4 9 2 10 16
# 2 7 16 5 8 9 10 11
# 12 19 18 8 7 11 15 12
# 1 20 18 17 16 15 14 13



