from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())

    tree[a].append(b)
    in_degree[b] += 1

result = []
queue = deque()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)
        result.append(i)

while queue:
    current = queue.popleft()
    for t in tree[current]:
        in_degree[t] -= 1
        if in_degree[t] == 0:
            queue.append(t)
            result.append(t)

print(*result)