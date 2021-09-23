import sys

input = sys.stdin.readline


n,d = map(int,input().split()) #n 지름길 수 , d 고속도로 총 길이

graph = list()

pos=[i for i in range(d+1)]


for i in range(n):
    s,e,l = map(int,input().split())
    graph.append([s,e,l])

graph.sort()

for j in graph:

    s,e,l = j

    if e <= d:
        pos[e] = min(pos[s] + l,pos[e])
        
    for k in range(s,d+1):
        pos[k] = min(pos[k-1] + 1 , pos[k])


print(pos[d])

