import collections 


def bfs(graph, start):

    visit = list()
    queue = list()

    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

def dfs(graph,start):
    visit = list()
    stack = list()

    stack.append(start)

    while stack:
        node = stack.pop()
        print(node)
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit  


n,m,v = map(int,input().split()) # n = 정점 , m = 간선,  v = 탐색을 시작할 정점 번호
graph = {}

for i in range(m):
    a,b = list(map(int, input().split()))
    if i == 0 :
        graph[a] = [b]
        graph[b] = [a]
    elif graph.get(a) == None:
        graph[a] = [b]
        graph[b] = [a]
    else:
        temp = list()
        if type(graph[a]) == int:
            temp.append(graph[a])
        else:
            for j in graph[a]:
                temp.append(j)
        temp.append(b)
        graph[a] = temp



print(dfs(graph, v))
#print(bfs(graph, v))

