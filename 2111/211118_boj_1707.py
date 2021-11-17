from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

def bfs(start):
    vertex[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for k in graph[cur]:
            if vertex[k] == 0:
                vertex[k] = -vertex[cur]
                queue.append(k)
            else:
                if vertex[k] == vertex[cur]:
                    return False
    return True

for test_case in range(K):
    V, E = map(int, input().split())
    correct = True
    graph = [[] for _ in range(V + 1)]
    vertex = [0 for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if vertex[i] == 0:
            if not bfs(i):
                correct = False
                break
    
    print("YES" if correct else "NO")
