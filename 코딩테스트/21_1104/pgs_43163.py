from collections import deque

def solution(begin, target, words):

    answer = 0
    
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin,0))
    
    while q:
        
        cur, depth = q.popleft()
        
        
        for w in words:

            diff = 0
            
            for i in range(len(w)):
                
                if cur[i] != w[i]:  
                    diff += 1
                    
            if (diff == 1) and (w == target):
                depth += 1
                return depth
            
            elif diff == 1:
                q.append((w, depth+1))
                
    return answer