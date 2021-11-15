
def find(target):
    
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    
    return parent[target]

def union(a, b):
    
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, costs):
    
    answer = 0
    
    global parent 
    
    parent = [i for i in range(n)]
    
    costs.sort(key=lambda x : x[2])

    for cost in costs:
        s, e, w = cost
        if find(s) != find(e):
            answer += w
            union(s, e)

    return answer