import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):

    q = list()

    distance = [INF] * (n + 1)
    distance[start] = 0

    heapq.heappush(q, (0, start))
    
    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

T = int(input())

for _ in range(T):

    INF = int(1e9)
    
    n,m,t = map(int,input().split()) #교차로, 도로, 목적지 후보 개수
    s,g,h = map(int,input().split()) #시작지 , G,H사이의 도로 통과

    graph = [[] for _ in range(n + 1)]

    answer_list = list()
    

    for _ in range(m):

        a, b, d = map(int, input().split())

        graph[a].append((b, d))
        graph[b].append((a, d))


    candidate_list = list()

    for _ in range(t):
        candidate_list.append(int(input()))


    s_dijk = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h) 

    for c in candidate_list:
        if s_dijk[g] + g_dijk[h] + h_dijk[c] == s_dijk[c] or s_dijk[h] + h_dijk[g] + g_dijk[c] == s_dijk[c]:
            answer_list.append(c)

    answer_list.sort()

    for answer in answer_list:
        print(answer, end=' ')
    print()