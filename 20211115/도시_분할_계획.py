import sys
input = sys.stdin.readline

#사이클 없애기
#부모가 같은 노드를 연결하면 사이클 생김

answer = 0
last = 0

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

edges = sorted(edges, key= lambda x: x[2])

parent = [x for x in range(N+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for a, b, c in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c
        last = c
    
#last: 마을을 두개로 나눌거니까 제일 비싼 길 하나 없애주기
print(answer - last)
