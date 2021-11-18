import sys

input = sys.stdin.readline

def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):

    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int,input().split())

graph = list()
selected = list()

parent = [0] * (n + 1)

answer = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append([cost, a, b])

for i in range(1, n + 1):
    parent[i] = i

graph.sort()

for cost, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        answer += cost
        selected.append(cost)

answer -= selected.pop()

print(answer)