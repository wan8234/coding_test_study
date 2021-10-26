import heapq

def solution(jobs):
    answer = 0
    
    start = -1
    time = 0
    count = 0    
    heap = []
    
    jobs.sort()
    
    while count < len(jobs):
        for j in jobs[count:]:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = time
            time += current[0]
            answer += time - current[1]
            count += 1
        else:
            time += 1
    
    answer = answer // len(jobs)    
    
    return answer