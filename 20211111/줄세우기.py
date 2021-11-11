import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
d = [0] * (N+1)
arr = [[] for _ in range(N+1)]
d[0] = -1
q = deque()

for _ in range(M):
    x, y = map(int, input().split())
    d[y] += 1
    arr[x].append(y)

for i in range(1, N+1):
    if d[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=" ")
    for i in arr[x]:
        d[i] -= 1
        if d[i] == 0:
            q.append(i)
