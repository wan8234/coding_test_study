# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# height = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# for _ in range(M):
#     tall, short = map(int, input().split())
#     height[tall][short] = 1

# for k in range(1, N + 1):
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
#                 height[i][j] = 1

# answer = 0
# for i in range(1, N + 1):
#     know = 0
#     for j in range(1, N + 1):
#         know += height[i][j] + height[j][i]
#     if know == N - 1:
#         answer += 1
# print(answer)

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
line = defaultdict(set)

for _ in range(M):
    a, b = map(int, input().split())
    line[a].add(b)

def bfs(start):
    queue = deque()
    queue.append(start)

    visit = [0] * (N + 1)
    visit[start] = 1
    while queue:
        current = queue.popleft()
        for i in line[current]:
            if not visit[i]:
                visit[i] = 1
                line[start].add(i)
                queue.append(i)

for i in range(1, N + 1):
    bfs(i)

def cnt(n):
    count = 0
    for key in line.keys():
        if n in line[key]:
            count += 1
    return count

print(len([k for k in line if len(line[k]) + cnt(k) == N - 1]))