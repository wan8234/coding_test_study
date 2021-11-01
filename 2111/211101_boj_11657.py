import sys
input = sys.stdin.readline
inf = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [inf] * (N + 1)
dist[1] = 0
flag = True

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def bellmanFord():
    global flag
    
    for count in range(N):
        for i in range(1, N + 1):
            for time, arrival in graph[i]:
                if dist[i] != inf and dist[arrival] > dist[i] + time:
                    dist[arrival] = dist[i] + time

                    if count == N - 1:
                        flag = False
bellmanFord()

if not flag:
    print(-1)
else:
    for d in dist[2:]:
        print(d if d != inf else -1)
    
