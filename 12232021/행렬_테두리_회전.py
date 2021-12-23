def rotate(graph, query):

    x1, y1, x2, y2 = query
    x1y1 = graph[x1][y1]
    x1y2 = graph[x1][y2]
    x2y1 = graph[x2][y1]
    x2y2 = graph[x2][y2]
    
    # 오른쪽 밀기
    for j in range(y2, y1, -1):
        graph[x1][j] = graph[x1][j-1]
    
    # 아래로 밀기
    for i in range(x2, x1, -1):
        if i == x1+1:
            graph[i][y2] = x1y2
        else:
            graph[i][y2] = graph[i-1][y2]
    # 왼쪽으로 밀기
    for j in range(y1, y2):
        if j == y2-1:
            graph[x2][j] = x2y2
        else:
            graph[x2][j] = graph[x2][j+1]
    # 위로 밀기
    for i in range(x1, x2):
        if i == x2-1:
            graph[i][y1] = x2y1
        else:
            graph[i][y1] = graph[i+1][y1]
            
def findMin(graph, query):
    min_num = len(graph) * len(graph[0])
    x1, y1, x2, y2 = query
    x1y1 = graph[x1][y1]
    x1y2 = graph[x1][y2]
    x2y1 = graph[x2][y1]
    x2y2 = graph[x2][y2]
    
    for i in range(x1, x2+1):
        min_num = min(min_num, graph[i][y1])
    for i in range(x1, x2+1):
        min_num = min(min_num, graph[i][y2])
    for j in range(y1, y2+1):
        min_num = min(min_num, graph[x1][j])
    for j in range(y1, y2+1):
        min_num = min(min_num, graph[x2][j])
    return min_num

def solution(rows, columns, queries):
    # graph 초기화
    graph = [[0]* (columns+1) for _ in range(rows+1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            graph[i][j] = (i-1)*columns + j  
            
    answer = []  

    for query in queries:
        rotate(graph, query)
        answer.append(findMin(graph, query))
    return answer
