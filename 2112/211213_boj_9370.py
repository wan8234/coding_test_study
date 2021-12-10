import heapq
import sys
input = sys.stdin.readline

inf = int(1e9)
T = int(input())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    dp = [inf] * (n + 1)
    dp[start] = 0

    while heap:
        weight, current = heapq.heappop(heap)
        for next_node, next_weight in city[current]:
            new_weight = weight + next_weight
            if new_weight < dp[next_node]:
                dp[next_node] = new_weight
                heapq.heappush(heap, [new_weight, next_node])
    
    return dp

for test_case in range(1, T + 1):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    city = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        city[a].append([b, d])
        city[b].append([a, d])

    goals = []
    for _ in range(t):
        goals.append(int(input()))
    
    s_dp = dijkstra(s)
    g_dp = dijkstra(g)
    h_dp = dijkstra(h)
    result = []

    for goal in goals:
        if s_dp[g] + g_dp[h] + h_dp[goal] == s_dp[goal] or s_dp[h] + h_dp[g] + g_dp[goal] == s_dp[goal]:
            result.append(goal)

    result.sort()
    print(*result)