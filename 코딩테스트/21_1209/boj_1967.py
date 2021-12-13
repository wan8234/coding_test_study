import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

distance = [-1] * (n + 1)

for _ in range(n-1):

    a,b,c = map(int,input().split())

    tree[a].append([b,c])
    tree[b].append([a,c])


def bfs(start):

    q = deque([start])

    visited = [-1] * (n + 1)
    visited[start[0]] = 0

    ret = (0, 0)

    while q:
        cur, dist = q.popleft()

        for i in tree[cur]:

            if visited[i[0]] != -1: 
                continue

            visited[i[0]] = visited[cur] + i[1]
            q.append((i[0], visited[i[0]]))

            if ret[1] < visited[i[0]]:
                ret = (i[0], visited[i[0]])

    return ret

length1 = bfs((1, 0))
answer = bfs((length1[0],0))

print(answer[1])