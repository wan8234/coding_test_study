def solution(brown, yellow):
    
    x = 3   
    answer = []
    
    while True :
        
        y = (brown + yellow) // x # x * y = b + y
                   
        if yellow == (x - 2) * (y - 2) :   
            
            if x >= y :
                
                answer = [x, y]

                return answer
            
            else:
                
                answer = [y, x]

                return answer
            
            break
            
        x += 1
        

