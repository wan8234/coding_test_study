import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[b] = a

    # if a < b:
    #     parent[b] = a
    # else:
    #     parent[a] = b

for _ in range(m):
    cal, a, b = map(int, input().split())

    if cal == 0:
        union_find(a, b)
    elif cal == 1:
        a = find_parent(a)
        b = find_parent(b)

        if a == b:
            print("YES")
        else:
            print("NO")