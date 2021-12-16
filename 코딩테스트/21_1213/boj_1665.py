import sys
import heapq

input = sys.stdin.readline

n = int(input())


max_heap = list()
min_heap = list()

answer = list()

for i in range(n):

    num = int(input())

    if len(min_heap)==len(max_heap):
        heapq.heappush(min_heap, (-num, num))
        
    else:
        heapq.heappush(max_heap, (num, num))

    if max_heap and min_heap[0][1] > max_heap[0][0]:

        min=heapq.heappop(max_heap)[0]
        max=heapq.heappop(min_heap)[1]

        heapq.heappush(min_heap, (-min, min))
        heapq.heappush(max_heap, (max, max))

    answer.append(min_heap[0][1])
    
for j in answer:
    print(j)