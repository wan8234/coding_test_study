from collections import deque

n, m, v = map(int, input().split())

vertex = [[] for _ in range(n + 1)] # save node connection data
visit = [0] * (n + 1) # save visited data
que = deque() # for bfs

for _ in range(m): # connection
    first, second = map(int, input().split())

    vertex[first].append(second)
    vertex[second].append(first)

for data in vertex:
    data.sort()

def dfs(v): # depth first search
    print(v, end = " ")
    visit[v] = 1
    for node in vertex[v]:        
        if visit[node] == 0:            
            dfs(node)

def bfs(v): # breadth fisrt search
    print(v, end = " ")
    visit[v] = 1
    que.append(vertex[v])

    while que:
        temp = que.popleft()
        for node in temp:
            if visit[node] == 0:
                print(node, end = " ")
                visit[node] = 1
                que.append(vertex[node])

dfs(v)
visit = [0] * (n + 1)
print()
bfs(v)

