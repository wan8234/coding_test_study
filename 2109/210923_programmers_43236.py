def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    left = 0
    right = distance
    length = len(rocks)
    many = length - n
    
    while left <= right:
        
        mid = (left + right) // 2        
        count = 0
        point = 0
        
        for r in rocks:
            if (r - point) < mid:
                continue
            else:
                point = r
                count += 1
                
        if count < many:
            right = mid - 1
        elif count >= many:            
            if answer < mid:
                answer = mid
            left = mid + 1       
    
    return answer