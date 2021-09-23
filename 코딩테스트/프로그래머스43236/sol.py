def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start, end = 1, distance
    
    while start <= end:
        
        mid = (start+end) // 2
        
        current = 0
        removed_rocks = 0
        
        for rock in rocks:
            if rock-current < mid:
                removed_rocks += 1
            else:
                current = rock
                
        if removed_rocks > n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
        
    return answer