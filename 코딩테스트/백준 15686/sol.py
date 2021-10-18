import sys
from itertools import combinations

input = sys.stdin.readline


n,m = map(int,input().split())

# 0 - blank, 1 - house, 2 - store


graph  = [list(map(int,input().split())) for _ in range(n)]

store = []
house = []
answer = float('inf')

for i in range(n):
    for j in range(n):

       if graph[i][j] == 2:
           store.append((i,j))

       elif graph[i][j] == 1:
           house.append((i,j))

dist = [[0 for _ in range(len(store))] for _ in range(len(house))]

for i in range(len(house)):
    for j in range(len(store)):
        dist[i][j] = abs(house[i][0]-store[j][0]) + abs(house[i][1]-store[j][1])

answer = float('inf')

for range_list in combinations(range(len(store)),m):
    tmp = 0
    for i in range(len(house)):

        min_val = float('inf')

        for j in range_list:

            if min_val > dist[i][j]:
                min_val = dist[i][j]

        tmp += min_val

    if answer > tmp:
        answer = tmp

print(answer)