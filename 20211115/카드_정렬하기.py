import sys
input = sys.stdin.readline
import heapq

n = int(input())
card = []
for _ in range(n):
    x = int(input())
    heapq.heappush(card, x)

answer = 0

if n == 1:
    print(answer)
else:
    for _ in range(n-1):
        x = heapq.heappop(card)
        y = heapq.heappop(card)
        heapq.heappush(card, x+y)
        answer += x+y
    print(answer)