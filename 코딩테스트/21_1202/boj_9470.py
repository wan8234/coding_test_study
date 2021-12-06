from collections import deque
import sys

input = sys.stdin.readline

t = int(input())


for i in range(t):

    K,M,P = map(int,input().split())

    #graph = [list(map(int,input().split())) for _ in range(P)]
    graph = [[] for _ in range(M+1)]
    indegree = [0] * (M+1)
    count = [[0, 0]] * (M + 1) 
    order = [0] * (M + 1)

    q = deque()

    for i in range(P):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, M + 1):
        if indegree[i] == 0:
            count[i] = [1, 1]
            q.append(i)
    
    while q:
        temp = q.popleft()

        if count[temp][1] >= 2: 
            order[temp] = count[temp][0] + 1
            
        else:
            order[temp] = count[temp][0]

        for second in graph[temp]:
            indegree[second] -= 1

            if count[second][0] == order[temp]: 
                count[second][1] += 1

            elif count[second][0] < order[temp]: 
                count[second] = [order[temp], 1]

            if indegree[second] == 0: 
                q.append(second)

    print(K,max(order))