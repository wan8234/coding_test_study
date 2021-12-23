def solution(rows, columns, queries):
    answer = []
    matrix = [[i+j*columns for i in range(1, columns+1)] for j in range(rows)]
    def rotate(q, m):
        mini = 1e9
        x1, y1, x2, y2 = q
        #deepcopy 쓰면 시간초과
        temp = [x[:] for x in matrix]
        for i in range(y1, y2):
            temp[x1-1][i] = m[x1-1][i-1]
            temp[x2-1][i-1] = m[x2-1][i]
            mini = min(mini, m[x1-1][i-1], m[x2-1][i])
        for i in range(x1, x2):
            temp[i][y2-1] = m[i-1][y2-1]
            temp[i-1][y1-1] = m[i][y1-1]
            mini = min(mini, m[i-1][y2-1], m[i][y1-1])
        answer.append(mini)
        return temp
    
    for q in queries:
        matrix = rotate(q, matrix)
    print(answer)
    return answer


# solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
# solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]])