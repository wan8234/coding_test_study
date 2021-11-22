import sys
input = sys.stdin.readline

n = int(input())
stars = []
graph = []

for i in range(n):
    x, y = map(float, input().split())
    for j, nx, ny in stars:
        d = (nx - x) ** 2 + (ny - y) ** 2
        graph.append((i, j, d ** 0.5))
    stars.append((i, x, y))

print(graph)

parent = [x for x in range(n+1)]

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
    
answer = 0
graph = sorted(graph, key= lambda x: x[2])

for a, b, c in graph:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += c

print(round(answer, 2))    