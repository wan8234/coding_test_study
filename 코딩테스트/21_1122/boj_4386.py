import sys
import math

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


n = int(input())
parent = [i for i in range(n + 1)]

answer = 0

star_cord = list()
star_edge = list()

for _ in range(n):
    star_cord.append(list(map(float,input().split())))


for i in range(n - 1):
    for j in range(i + 1, n):
        star_edge.append((math.sqrt((star_cord[i][0] - star_cord[j][0])**2 + (star_cord[i][1] - star_cord[j][1])**2), i, j))


star_edge.sort()

for edge in star_edge:
    c,x,y = edge

    if find(x) != find(y):
        union(x,y)
        answer += c


print(round(answer,2))