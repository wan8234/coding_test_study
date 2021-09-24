import heapq
import sys
input = sys.stdin.readline

inf = int(1e9)

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
city = [inf] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    bus[s].append((e, w))

start, end = map(int, input().split())

city[start] = 0
heap = []
heapq.heappush(heap, [0, start])

while heap:
    w, c = heapq.heappop(heap)

    if city[c] < w: # can overcome time over
        continue
    
    for next_city, weight in bus[c]:
        new_weight = w + weight
        if new_weight < city[next_city]:
            city[next_city] = new_weight
            heapq.heappush(heap, [new_weight, next_city])

print(city[end])

