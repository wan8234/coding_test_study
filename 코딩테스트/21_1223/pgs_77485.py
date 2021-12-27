def solution(rows, columns, queries):
    answer = []
    table = []

    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    

    for query in queries:

        query = [x-1 for x in query] 
        tmp = table[query[0]][query[1]] 
        min_value = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):

            table[i-1][query[1]] = table[i][query[1]]
            min_value = min(min_value, table[i][query[1]])

        # bottom
        for i in range(query[1]+1, query[3]+1):

            table[query[2]][i-1] = table[query[2]][i]
            min_value = min(min_value, table[query[2]][i])

        # right
        for i in range(query[2]-1, query[0]-1, -1):

            table[i+1][query[3]] = table[i][query[3]]
            min_value = min(min_value, table[i][query[3]])

        # top
        for i in range(query[3]-1, query[1]-1, -1):

            table[query[0]][i+1] = table[query[0]][i]
            min_value = min(min_value, table[query[0]][i])

        table[query[0]][query[1]+1] = tmp
        
        answer.append(min_value)
    
    return answer