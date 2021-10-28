import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

def bfs():

    visited[N] = 0
    cnt[N] = 1

    dq = [N]
    dq = deque(dq)
    while dq:
        x = dq.popleft()
        for i in [x-1, x+1, x*2]:
            if i < 0 or i > 100000:
                continue
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                cnt[i] = cnt[x]
                dq.append(i)
            elif visited[i] == visited[x] + 1:
                cnt[i] += cnt[x]

visited = [-1] * 100001
cnt = [0] * 100001

bfs()
print(visited[K])
print(cnt[K])