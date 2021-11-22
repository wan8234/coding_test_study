import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    d = round((x**2 + y**2)**0.5, 2)
    return d


n = int(input())
parent = [i for i in range(n + 1)]

arr = []
for _ in range(n):
    x, y = map(float, input().split())
    arr.append([x,y])

#가중치 계산
E = []
for i in range(n - 1):
    for j in range(i + 1, n):
        a = arr[i]
        b = arr[j]
        E.append((distance(a,b), i, j))

E.sort()

res = 0
for cost, x, y in E:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        res += cost
print(round(res, 2))

