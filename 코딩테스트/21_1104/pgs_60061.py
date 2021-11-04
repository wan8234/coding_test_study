def check(ans):
    
    for i in range(len(ans)):
        
        x, y, a = ans[i]
        
        if a == 0: 
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
            
        if a == 1:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True
        
def solution(n, build_frame):
    answer = []
    
    for i in range(len(build_frame)):
        
        x, y, a, b = build_frame[i]
        
        if b == 0: # delete 
            
            answer.remove([x, y, a])
            
            if check(answer) == False:
                answer.append([x, y, a])
                
        elif b == 1: # add
            
            answer.append([x, y, a]) 
            
            if check(answer) == False:
                answer.remove([x, y, a])
                
    
    answer = sorted(answer)
                
    return answer