def solution(tickets):
    answer = []
    route = dict()
    start = ["ICN"]
    
    for i in tickets:
        route[i[0]] = route.get(i[0],[]) + [i[1]]
    
    for j in route:
        route[j].sort(reverse = True)
        
    while start:
        top = start[-1]

        if top not in route or len(route[top]) ==0:
            answer.append(start.pop())

        else:
            start.append(route[top][-1])
            route[top].pop()

    answer.reverse()
    
    return answer