def solution(s):
    answer = len(s)
    
    if answer == 1: 
        return 1

    
    for i in range(1,(len(s)//2) +1):
        
        comp = ''
        prev = s[0:i]
        count = 1
        
        for j in range(i,len(s),i):
            
            if prev == s[j:j+i]:
                count += 1
                
            else:
                comp += str(count) + prev if count >= 2 else prev
                prev = s[j:j+i]
                count = 1
   
        comp += str(count) + prev if count >= 2 else prev
        answer = min(answer,len(comp))

        
    return answer