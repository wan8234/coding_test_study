import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def findParent(i):
    if arr[i] != i:
        arr[i] = findParent(arr[i])
    return arr[i]


def unionParent(x, y):
    x = findParent(x)
    y = findParent(y)

    if x == y:
        return

    if x > y:
        arr[x] = y
    else:
        arr[y] = x


n,m = map(int,input().split())
arr = [i for i in range(n+1)]

lines=[]
for _ in range(m):
    x, a, b = map(int,input().split()) 
    lines.append((x, a, b))

for l in lines:
    x, a, b = l

    if x == 0: 
        unionParent(a,b)
    elif x == 1: 
        if findParent(a) == findParent(b):
            print('YES')
        else:
            print('NO')
