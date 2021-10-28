import heapq

def solution(jobs):
    
    answer,time,end,count = 0,0,-1,0
    
    n = len(jobs)
    q = list()
    
    while count < n:
        
        for i in range(len(jobs)):   
            
            if end < jobs[i][0] <= time:           
                answer += (time - jobs[i][0])
                heapq.heappush(q,jobs[i][1])
                
        if q:
            answer += (len(q) * q[0])
            end = time
            time += heapq.heappop(q)
            count += 1
            
        else:
            time += 1
    
    answer = answer//n

    return answer