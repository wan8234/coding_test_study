import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [x for x in range(n+1)]

def find_parent(x):
    if arr[x] != x:
        arr[x] = find_parent(arr[x])
    return arr[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return

    if a < b:
        arr[b] = a
    else:
        arr[a] = b


for _ in range(m):
    t, x, y = map(int, input().split())

    if t == 0:
        union_parent(x, y)
    elif t == 1:
        if find_parent(x) == find_parent(y):
            print("YES")
        else:
            print("NO")