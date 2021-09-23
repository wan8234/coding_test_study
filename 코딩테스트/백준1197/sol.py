import sys
import heapq

input = sys.stdin.readline
 
v, e = map(int, input().split())
visited = [False]*(v+1)
Elist = [[] for _ in range(v+1)]
heap = [[0, 1]]
for _ in range(e):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
 
answer = 0
cnt = 0
while heap:
    if cnt == v:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)
 
print(answer)
