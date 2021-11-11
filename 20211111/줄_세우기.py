import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

d = [0] * (N+1)
c = [[] for _ in range(N+1)]

d[0] = -1

for _ in range(M):
    x, y = map(int, input().split())
    d[y] += 1
    c[x].append(y)

dq = deque()
for i in range(1, N+1):
    if d[i] == 0:
        dq.append(i)

while dq:
    x = dq.popleft()
    print(x, end=" ")
    for i in c[x]:
        d[i] -= 1
        if d[i] == 0:
            dq.append(i)
