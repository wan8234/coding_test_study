import sys, heapq
input = sys.stdin.readline

n = int(input())
data = []
result = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(data, -x)
    else:
        if data:            
            result.append(-heapq.heappop(data))
        else:
            result.append(0)

for i in result:
    print(i)