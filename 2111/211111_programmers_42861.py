#### KRUSKAL 1 ####
def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])
    connect = set([costs[0][0]])
    
    while len(connect) != n:
        for a, b, cost in costs:
            if a in connect and b in connect:
                continue
            if a in connect or b in connect:
                connect.update([a, b])
                answer += cost
                break
                
    return answer

#### KRUSKAL 2 ####
def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    count = 0

    for a, b, cost in costs:
        if find(a, parent) != find(b, parent):
            answer += cost
            parent[find(b, parent)] = a
            count += 1
        if count == n - 1:
            break

    return answer

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

#### HEAP ####
import heapq

def solution(n, costs):
    answer = 0
    from_to = [[] for _ in range(n)]
    visit = [0] * n
    priority = []

    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))

    heapq.heappush(priority, (0, 0))
    while 0 in visit:
        cost, start = heapq.heappop(priority)
        if visit[start]:
            continue

        visit[start] = 1
        answer += cost
        for end, cost in from_to[start]:
            if visit[end]:
                continue
            else:
                heapq.heappush(priority, (cost, end))
    
    return answer

#### FAIL ####
# def solution(n, costs):
#     answer = 0
    
#     costs.sort(key = lambda x : x[2])
#     island = [0] * n
#     count = []
#     total = (n * (n - 1)) // 2
    
#     for a, b, cost in costs:
#         if island[a] == 0 or island[b] == 0:
#             if a not in count:
#                 count.append(a)
#             if b not in count:
#                 count.append(b)
#             answer += cost
#         if sum(count) == total:
#             break
                
#     return answer