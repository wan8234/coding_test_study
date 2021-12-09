import sys


input = sys.stdin.readline

def find(a):

    if a == parent[a]: 
        return a

    p = find(parent[a]) 
    parent[a] = p 

    return parent[a]


def union(a,b):

    a = find(a) 
    b = find(b) 

    if a == b: 
        return
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,input().split())

parent = [i for i in range(n)]

answer = 0

for i in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i+1)
        sys.exit(0)

    union(a, b)

print(0)
