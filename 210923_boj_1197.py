### Prim ###
import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
visit = [False] * (v + 1)
edge = [[] for _ in range(v + 1)]
heap = [[0, 1]]

for _ in range(e):
    f, s, w = map(int, input().split())
    edge[f].append([w, s])
    edge[s].append([w, f])

result = 0
count = 0

while heap:
    if count == v:
        break
    w, f = heapq.heappop(heap)
    if not visit[f]:
        visit[f] = True
        result += w
        count += 1
        for i in edge[f]:
            heapq.heappush(heap, i)

print(result)


### Kruskal ###
# import sys
# input = sys.stdin.readline

# v, e = map(int, input().split())

# root = [i for i in range(v + 1)]
# edge = []
# result = 0

# for i in range(e):
#     edge.append(list(map(int, input().split())))

# edge.sort(key = lambda x : x[2])

# def find(x):
#     if x != root[x]:
#         root[x] = find(root[x])
#     return root[x]

# for f, s, w in edge:
#     f_root = find(f)
#     s_root = find(s)

#     if f_root != s_root:
#         if f_root > s_root:
#             root[f_root] = s_root
#         else:
#             root[s_root] = f_root
#         result += w

# print(result)
