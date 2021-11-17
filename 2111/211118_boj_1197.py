import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
vertex = [0] * (V + 1)
edges = [[] for _ in range(V + 1)]
heap = [[0, 1]]
result = 0
count = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges[a].append([cost, b])
    edges[b].append([cost, a])

while heap:
    if count == V:
        break
    cost, a = heapq.heappop(heap)
    if not vertex[a]:
        vertex[a] = 1
        result += cost
        count += 1
        for i in edges[a]:
            heapq.heappush(heap, i)
    
print(result)


#### KRUSKAL #### 
import sys
input = sys.stdin.readline

v, e = map(int, input().split())

root = [i for i in range(v + 1)]
edge = []
result = 0

for i in range(e):
    edge.append(list(map(int, input().split())))

edge.sort(key = lambda x : x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

for f, s, w in edge:
    f_root = find(f)
    s_root = find(s)

    if f_root != s_root:
        if f_root > s_root:
            root[f_root] = s_root
        else:
            root[s_root] = f_root
        result += w

print(result)
