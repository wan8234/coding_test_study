import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [x for x in range(n+1)]

def find_parent(x):
    if arr[x] != x:
        arr[x] = find_parent(arr[x])
    return arr[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        arr[y] = x
    else:
        arr[x] = y
    

for i in range(1, m+1):
    x, y = map(int, input().split())
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
    else:
        print(i)
        break
else:
    print(0)
