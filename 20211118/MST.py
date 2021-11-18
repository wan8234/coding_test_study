'''
Prim
임의의 정점 하나를 선택해서 시작
선택한 정점과 인접하는 정점들 중 가중치가 최소인 정점을 선택
모든 정점이 선택될 때까지 반복
'''

from heapq import heappush, heappop
import sys
input=sys.stdin.readline

def prim(start, cost):
    visited = [0] * (V + 1) 
    q = [[cost, start]] 
    res = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    
    while cnt < V: # 간선의 개수 최대는 V-1
        cost, v = heappop(q)
        if visited[v]:
            continue # 이미 방문한 정점이면 지나감
        visited[v] = 1 # 방문안했으면 방문처리
        res += cost
        cnt += 1 
        for i in graph[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, i) # 힙에 넣어줌
    return res

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])

print(prim(1, 0))
