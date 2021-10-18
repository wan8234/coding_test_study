import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

m_cost = float('inf')
    
def dfs(start,cur,cost,visited):

    global m_cost, graph

    if start == cur and False not in visited:

        m_cost = min(m_cost,cost)

    
    for i in range(n):

        if graph[cur][i] != 0 and visited[i] == False:

            if cost > m_cost:
                return

            visited[i] = True
            dfs(start, i, cost+graph[cur][i],visited)
            visited[i] = False         
             
    return m_cost


print(dfs(0,0,0,visited))