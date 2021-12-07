from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)

for i in range(N - 1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append((b, w))
    tree[b].append((a, w))

def bfs(start, flag):
    queue = deque()    
    queue.append(start)
    visit = [-1] * N
    visit[start] = 0

    while queue:
        current = queue.popleft()
        for node, weight in tree[current]:
            if visit[node] == -1:
                visit[node] = visit[current] + weight
                queue.append(node)

    if flag == 1:
        return visit.index(max(visit))
    else:
        return max(visit)

result = bfs(0, 1)
result = bfs(result, 0)

print(result)