import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


n = int(input())
parent = [0] * (n + 1)

data = []
edge = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        edge.append((data[i][j], i, j))

edge.sort()

for e in edge:
    cost, a, b = e
    # 사이클이 발생하지 않는 경우에만 집합에 포함 (연결)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)