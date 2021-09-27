import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = 987654321

n = int(input())
m = int(input())

data = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
heap = []

for _ in range(m):
    s,e,c = map(int,input().split())
    data[s].append((e,c))

start,end = map(int,input().split())


dist[start] = 0

heappush(heap, [0, start])

while heap:

    w, n = heappop(heap)

    if dist[n] < w:
        continue

    for n_c, weight in data[n]:
        n_w = weight + w

        if n_w < dist[n_c]:
            dist[n_c] = n_w
            heappush(heap, [n_w, n_c])


print(dist[end])