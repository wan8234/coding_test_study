import sys
import heapq

input = sys.stdin.readline

n = int(input()) #size of seq

seq = list(map(int, input().split()))

answer = list()

heapq.heapify(seq)

for _ in range(n):

    temp = heapq.heappop(seq)
    
    if temp not in answer:
        answer.append(temp) 


print(answer)
print(len(answer))


# 시간 초과