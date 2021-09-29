from collections import deque

def solution(n, computers):
    answer = 0
    visit = [0] * n
    
    for i in range(n):
        if visit[i] == 0:
            bfs(n, computers, i, visit)
            answer += 1
        
    return answer

def bfs(n, computers, i, visit):
    visit[i] = 1
    q = deque()
    q.append(i)
    
    while q:
        i = q.popleft()
        visit[i] = 1
        
        for net in range(n):
            if net != i and computers[i][net] == 1:
                if visit[net] == 0:
                    q.append(net)
        
    