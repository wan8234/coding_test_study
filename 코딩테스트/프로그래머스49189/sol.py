from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[]* n for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0]*(n+1)
    visited[1] = 1
    queue = deque([1])
    while(queue):
        n = queue.popleft()
    
        for i in graph[n]:
            if visited[i]==0:
                queue.append(i)
                visited[i] = visited[n]+1
                
    answer = visited.count(max(visited))
    return answer
