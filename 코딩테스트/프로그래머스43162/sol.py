from collections import deque

def bfs(n,computers,start,visit):
    queue = deque([start])
    
    visit[start] = True
    
    while queue:
        v = queue.popleft()
        
        for i in range(n):
            if not visit[i] and computers[v][i] == 1:
                queue.append(i)
                visit[i] = True
    
    
def solution(n, computers):
    
    answer = 0
    
    visit = [False for i in range(n)]
    
    for i in range(n):
        if not visit[i]:
            bfs(n,computers,i,visit)
            answer += 1
            
    return answer