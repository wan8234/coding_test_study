import math
import sys
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [i for i in range(N + 1)]

star = []
edge = []
result = 0

for _ in range(N):
    star.append(list(map(float, input().split())))

for i in range(N - 1):
    for j in range(i + 1, N):
        edge.append((math.sqrt((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2), i, j))

edge.sort()

for cost, a, b in edge:
    if find_parent(a) != find_parent(b):
        union_find(a, b)
        result += cost

print(round(result, 2))