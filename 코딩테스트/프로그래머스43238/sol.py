def solution(n, times):
    
    answer = 0
    
    left,right = 1, max(times)*n
    
    while left <= right:
        
        mid = (left+right) // 2
        people = 0
        
        for i in times:
            
            people += mid // i
            
            if people >= n:
                answer = mid
                right = mid -1
                break
        
        if people < n:
            left = mid + 1
                
    return answer