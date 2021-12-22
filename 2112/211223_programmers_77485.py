def solution(rows, columns, queries):
    answer = []
    table = []
    
    for i in range(rows):
        line = []
        for j in range(columns):
            line.append(i * columns + j + 1)
        table.append(line)
    
    for query in queries:
        temp = table[query[0] - 1][query[1] - 1]
        minimum = temp
        
        for i in range(query[0] - 1, query[2] - 1):
            table[i][query[1] - 1] = table[i + 1][query[1] - 1]
            minimum = min(minimum, table[i][query[1] - 1])
        
        for i in range(query[1] - 1, query[3] - 1):
            table[query[2] - 1][i] = table[query[2] - 1][i + 1]
            minimum = min(minimum, table[query[2] - 1][i])
            
        for i in range(query[2] - 1, query[0] - 1, -1):
            table[i][query[3] - 1] = table[i - 1][query[3] - 1]
            minimum = min(minimum, table[i][query[3] - 1])
            
        for i in range(query[3] - 1, query[1] - 1, -1):
            table[query[0] - 1][i] = table[query[0] - 1][i - 1]
            minimum = min(minimum, table[query[0] - 1][i])
        
        table[query[0] - 1][query[1]] = temp
        answer.append(minimum)
            
    return answer