import sys
input = sys.stdin.readline


# 특정 원소가 속한 집합 find
def findParent(arr, i):
    if arr[i] != i:
        arr[i] = findParent(arr, arr[i])
    return arr[i]


# 두 원소가 속한 집합 union
def unionParent(arr, x, y):
    x = findParent(arr, x)
    y = findParent(arr, y)

    if x > y:
        arr[x] = y
    else:
        arr[y] = x


N, M = map(int, input().split())
arr = [i for i in range(N+1)]

lines = []
for _ in range(M):
    x, y, c = map(int, input().split())
    lines.append((c, x, y))
lines.sort()

res = 0
last = 0 # 마지막 길은 제거

for e in lines:
    c, x, y = e
    #닫히지 않으면 union
    if findParent(arr, x) != findParent(arr, y):
        unionParent(arr, x, y)
        res += c
        last = c

print(res -last)
