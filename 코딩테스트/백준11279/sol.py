import heapq,sys

input = sys.stdin.readline

n = int(input())

heap = list()

res = list()

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap,-x)
    else:
        if heap:
            res.append(-(heapq.heappop(heap)))
        else:
            res.append(0)

print(res)