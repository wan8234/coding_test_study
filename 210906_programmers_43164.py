def solution(tickets):
    answer = []
    city = {}
    stack = ["ICN"]
    
    for t in tickets:
        city[t[0]] = city.get(t[0], []) + [t[1]]    
    for c in city:
        city[c].sort()   
    
    while stack:
        cur = stack[-1]
                
        if cur in city and city[cur]:     
            stack.append(city[cur].pop(0))
        else:
            answer.append(stack.pop())
    
    return answer[::-1]