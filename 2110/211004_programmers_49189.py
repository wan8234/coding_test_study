from collections import defaultdict, deque

def solution(n, edge):
    answer = 0    
    distance = [0] * (n + 1)
    edge.sort()
    
    dict = defaultdict(list)
    for first, second in edge:
        dict[first].append(second)
        dict[second].append(first)
    
    q = deque()
    q.append(1)
    distance[1] = 1
    
    while q:
        vertex = q.popleft()
        for e in dict[vertex]:
            if distance[e] == 0:
                q.append(e)
                distance[e] = distance[vertex] + 1
    
    maximum = max(distance)
    answer = distance.count(maximum)
    
    return answer