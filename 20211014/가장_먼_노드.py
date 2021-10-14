from collections import deque

def solution(n, edge):
    answer = 0
    matrix = [[] for _ in range(n+1)]

    for x, y in edge:
        matrix[x].append(y)
        matrix[y].append(x)
    
    dq = [(1, 0)]
    dq = deque(dq)
    passed = [-1] * (n+1)
    passed[1] = 0
    maxi = 0
    
    while dq:
        x, l = dq.popleft()
        for y in matrix[x]:
            if passed[y] == -1:
                passed[y] = l+1
                dq.append((y, l+1))
                
    answer = passed.count(max(passed))
    return answer