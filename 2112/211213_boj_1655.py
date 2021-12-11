import heapq
import sys
input = sys.stdin.readline

N = int(input())
left = []
right = []
result = []

for _ in range(N):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][0]:
        minimum = heapq.heappop(right)[1]
        maximum = heapq.heappop(left)[1]

        heapq.heappush(left, (-minimum, minimum))
        heapq.heappush(right, (maximum, maximum))

    result.append(left[0][1])

for r in result:
    print(r)        
