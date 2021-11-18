import sys
input = sys.stdin.readline

#크루스칼
answer = 0

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

edges = sorted(edges, key= lambda x: x[2])
parent = [x for x in range(N+1)]

def find_prarent(x):
    if parent[x] != x:
        parent[x] = find_prarent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_prarent(a)
    b = find_prarent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for a, b, c in edges:
    if find_prarent(a) != find_prarent(b):
        union_parent(a, b)
        answer += c

print(answer)
    