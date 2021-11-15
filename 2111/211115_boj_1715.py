import heapq as h

n = int(input())
card = []

# for _ in range(n):
#     h.heappush(card, int(input()))

for _ in range(n):
    card.append(int(input()))

h.heapify(card)
result = 0

while len(card) != 1:
    first = h.heappop(card)
    second = h.heappop(card)

    temp = first + second
    result += temp
    h.heappush(card, temp)

print(result)