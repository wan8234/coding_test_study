import sys
import heapq
input = sys.stdin.readline

N = int(input())

a, b = [], []
answer = []

for i in range(N):
    num = int(input())
    
    if len(a) == len(b):
        # a num 대입
        heapq.heappush(a, -num)
    else:
        # 아니면 b에 num 대입
        heapq.heappush(b, num)

    if b and a[0] * -1 > b[0]:
        max_value = heapq.heappop(a) * -1
        min_value = heapq.heappop(b)
        heapq.heappush(a, min_value * -1)
        heapq.heappush(b, max_value)
    
    answer = a[0] * -1
    print(answer)
