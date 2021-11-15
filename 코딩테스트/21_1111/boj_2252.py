import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

key = [[] for i in range(n+1)]
in_deg = [0] * (n+1)

for _ in range(m):

    x,y = map(int,input().split())
    
    key[x].append(y)
    in_deg[y] += 1

answer = list()
q = deque()


for i in range(1,n+1):

    if in_deg[i] == 0:
        q.append(i)

while q:

    node = q.popleft()
    answer.append(node)
    
    for i in key[node]:

        in_deg[i] -= 1

        if in_deg[i] == 0:
            q.append(i)

print(*answer)
