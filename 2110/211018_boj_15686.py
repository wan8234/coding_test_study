from itertools import combinations
import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

markets = list(combinations(chicken, m))

def get_sum(market):
    result = 0
    for hx, hy in house:
        temp = inf
        for mx, my in market:
            temp = min(temp, abs(hx - mx) + abs(hy - my))
        result += temp
    return result

result = inf

for market in markets:
    result = min(result, get_sum(market))

print(result)
