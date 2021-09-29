def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        
        for t in times:
            temp += mid // t
            if temp >= n:
                break
        
        if temp >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer