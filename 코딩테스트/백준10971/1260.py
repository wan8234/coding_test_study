from collections import deque
import sys
 
n, m, start = map(int, sys.stdin.readline().strip().split())
 
edge = [[] for _ in range(n + 1)]
 
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for e in edge:
    e.sort()

visited = []

def dfs(start_node,visited):

    visited.append(start_node)

    for w in edge[start_node]:

        if w not in visited:
            visited = dfs(w,visited)

    return visited


def bfs(start_node,visited):

    visited.append(start_node)
    queue = deque([start_node])

    while queue:

        v = queue.popleft()

        for w in edge[v]:
            
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


print(*dfs(start,visited))
visited.clear()
print(*bfs(start,visited))

