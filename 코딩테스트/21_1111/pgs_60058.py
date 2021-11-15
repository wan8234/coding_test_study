def separate(w):
    
    left,right = 0,0
    
    for i in range(len(w)):
        
        if w[i] == '(':
            left += 1
        else:
            right += 1
            
        if left == right:
            return w[:i + 1], w[i + 1:]
 
def check_balance(u):
    
    stack = []
    left = '('
    

    for p in u:
        if p == left:
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True
 
 
def solution(w):

    if len(w) == 0:
        return ""    

    u, v = separate(w)

    if check_balance(u):
        return u + solution(v)

    else:

        answer = '('
        answer += solution(v)
        answer += ')'
        

        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        return answer