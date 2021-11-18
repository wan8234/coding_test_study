import collections
import sys


input = sys.stdin.readline

for _ in range(int(input())):

    V, E = map(int, input().split())

    graph = [[] for i in range(V+1)] 
    visited = [0] * (V+1)

    for _ in range(E):

        a,b = map(int, input().split())

        graph[a].append(b) 
        graph[b].append(a) 


    q = collections.deque()

    group = 1
    isTrue = True

    for i in range(1, V+1):

        if visited[i] == 0: 

            q.append(i)
            visited[i] = group

            while q:

                v = q.popleft()

                for w in graph[v]:

                    if visited[w] == 0: 
                        q.append(w)
                        visited[w] = -1 * visited[v] 

                    elif visited[v] == visited[w]: 
                        isTrue = False

    print('YES' if isTrue else 'NO')