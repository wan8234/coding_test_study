import sys

input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

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

for _ in range(m):

    x, a, b = map(int,input().split()) 

    if x == 0: 
        union(a,b)
        
    elif x == 1: 
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')






