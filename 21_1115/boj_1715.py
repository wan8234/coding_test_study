import sys
import heapq

input = sys.stdin.readline

n = int(input())
answer = 0 

card_list = list()

for _ in range(n):
    card_list.append(int(input()))

heapq.heapify(card_list)


while card_list:

    if len(card_list) > 1:
        a = heapq.heappop(card_list)
        b = heapq.heappop(card_list)

        heapq.heappush(card_list,a+b)

        answer += (a+b)

    else:
        break



print(answer)