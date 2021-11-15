import heapq

N = int(input())
res = 0
arr=[]
for i in range(N):
    heapq.heappush(arr, int(input()))

while len(arr) != 1:
    min1 = heapq.heappop(arr)
    min2 = heapq.heappop(arr)
    min_sum = min1 + min2
    res += min_sum
    heapq.heappush(arr, min_sum)

print(res)

