import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

chicken = []
house = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))

c = list(combinations(chicken, M))

answer = 100000000
for nod in c:
    total = 0
    for hx, hy in house:
        mini = 100
        for x, y in nod:
            
            dis = abs(x-hx) + abs(y-hy)
            if dis < mini:
                mini = dis
        total += mini
    if total < answer:
        answer = total

print(answer)