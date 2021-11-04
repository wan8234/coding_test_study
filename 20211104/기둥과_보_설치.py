def solution(n, build_frame):
    answer = []

    col = [[0] * (n+1) for _ in range(n+1)]
    row = [[0] * (n+1) for _ in range(n+1)]
    
    def rowcheck(x, y, m):
        if m == 0 and row[x][y] == 0:
            return True
        if y > 0 and col[x][y-1] == 1:
            return True
        if x < n and y > 0 and col[x+1][y-1] == 1:
            return True
        if 0 < x < n and row[x-1][y] == 1 and row[x+1][y] == 1:
            return True
        return False

    def colcheck(x, y, m):
        if m == 0 and col[x][y] == 0:
            return True
        if y == 0:
            return True
        if row[x][y] == 1:
            return True
        if x > 0 and row[x-1][y] == 1:
            return True
        if y > 0 and col[x][y-1] == 1:
            return True
        return False

    for x, y, t, m in build_frame:
        if m == 1:
            if t == 0:
                if colcheck(x, y, m):
                    col[x][y] = 1
                    answer.append([x, y, 0])
            else:
                if rowcheck(x, y, m):
                    row[x][y] = 1
                    answer.append([x, y, 1])
        else:
            if t == 0:
                col[x][y] = 0
                if rowcheck(x-1, y+1, m) and rowcheck(x, y+1, m) and colcheck(x, y+1, m):
                    answer.remove([x, y, 0])
                else:
                    col[x][y] = 1
            else:
                row[x][y] = 0
                if colcheck(x, y, m) and colcheck(x+1, y, m) and rowcheck(x-1, y, m) and rowcheck(x+1, y, m):
                    answer.remove([x, y, 1])
                else:
                    row[x][y] = 1

    return sorted(answer)

#print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))